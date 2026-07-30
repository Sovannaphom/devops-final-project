#!/usr/bin/env python3
"""
Patch Kubespray etcd tasks to fix list evaluation under jinja2_native=True.

etcd_admin_certs and etcd_node_certs contain nested lists.
Legacy with_items implicitly flattened nested lists, but loop: does not.
Under jinja2_native=True, with_items passes the inner list as a single string item.
This patch converts with_items blocks to use loop: "{{ (...) | flatten }}" so that
nested cert lists are flattened into individual file path strings.
"""
import glob
import os
import sys

def patch_file(path):
    if not os.path.exists(path):
        return False

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    orig_content = content
    lines = content.replace("\r\n", "\n").splitlines()

    combined_loop = 'loop: "{{ (etcd_admin_certs | default([]) + etcd_node_certs | default([])) | flatten }}"'
    admin_loop = 'loop: "{{ (etcd_admin_certs | default([])) | flatten }}"'
    node_loop = 'loop: "{{ (etcd_node_certs | default([])) | flatten }}"'

    new_lines = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]
        if "with_items:" in line:
            indent_len = len(line) - len(line.lstrip())
            indent = " " * indent_len

            j = i + 1
            has_admin = "etcd_admin_certs" in line
            has_node = "etcd_node_certs" in line

            while j < len(lines):
                next_line = lines[j]
                next_indent = len(next_line) - len(next_line.lstrip())
                if next_line.strip().startswith("-") or (next_line.strip() and next_indent > indent_len):
                    if "etcd_admin_certs" in next_line:
                        has_admin = True
                    if "etcd_node_certs" in next_line:
                        has_node = True
                    j += 1
                else:
                    break

            if has_admin and has_node:
                new_lines.append(indent + combined_loop)
                i = j
                changed = True
                continue
            elif has_admin:
                new_lines.append(indent + admin_loop)
                i = j
                changed = True
                continue
            elif has_node:
                new_lines.append(indent + node_loop)
                i = j
                changed = True
                continue

        new_lines.append(line)
        i += 1

    final_content = "\n".join(new_lines) + "\n"

    if changed or final_content != orig_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(final_content)
        print(f"Patched: {path}")
        return True

    return False

def main():
    target_files = glob.glob("/opt/kubespray/roles/etcd/tasks/*.yml")
    total_changed = 0
    for f in target_files:
        if patch_file(f):
            total_changed += 1

    print(f"Final changed={total_changed > 0}")

if __name__ == "__main__":
    main()
