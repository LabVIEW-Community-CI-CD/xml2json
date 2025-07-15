#!/usr/bin/env python3
"""
verify-hashes.py - Verify that each issue file's content_hash matches its body content.

This script iterates through all Markdown issue files under .gpt/issues/phase*/,
calculates the SHA-256 hash of the file body (excluding the YAML front-matter),
and compares it against the content_hash field in the front-matter.
Reports any mismatches and exits with status 1 if any are found.
"""

import os
import glob
import hashlib
import yaml
import sys

def compute_sha256(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def verify_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    if not text.startswith('---'):
        print(f"Skipping {path}: no front-matter found.")
        return True
    # Split front-matter
    parts = text.split('---', 2)
    # After first '---', second part ends front-matter
    if len(parts) < 3:
        print(f"Skipping {path}: front-matter incomplete.")
        return True
    _, front_matter, body = parts[0], parts[1], parts[2]
    meta = yaml.safe_load(front_matter)
    expected_hash = meta.get('content_hash')
    if expected_hash is None:
        print(f"Skipping {path}: no content_hash in front-matter.")
        return True
    # Remove leading newline if present in body
    if body.startswith('\n'):
        body = body[1:]
    actual_hash = compute_sha256(body)
    if actual_hash != expected_hash:
        print(f"Hash mismatch in {path}: expected {expected_hash}, got {actual_hash}")
        return False
    return True

def main():
    all_ok = True
    # Find all markdown issue files in .gpt/issues/phase*/ directories
    issue_files = glob.glob(os.path.join('.gpt', 'issues', 'phase*', '*.md'))
    for path in sorted(issue_files):
        ok = verify_file(path)
        all_ok = all_ok and ok
    if not all_ok:
        sys.exit(1)
    print("All content_hash fields match file bodies.")

if __name__ == '__main__':
    main()
