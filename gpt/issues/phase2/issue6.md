---
issue_id: 6
title: "Update deliverable wording to remove Marketplace publication"
phase: 2
status: open
tags: ["insight-synch", "deliverables", "vscext"]
created_at: "2025-07-10T09:05:00Z"
content_hash: 4e9e2b32d59f99b1331c8a9d009aa226295c5be85f78e87bf1f621063e6d8900
---
The SRS mentions publishing the VS Code extension to the Marketplace by T+25 days. However, SRS §7.2 NFR-E-2 requires that the extension be side-loaded and not publicly published. Update the deliverables section to:

- Remove any reference to Marketplace publication as a required deliverable.
- State that the extension (.vsix) will be packaged and distributed via the internal artifact feed instead of the public Marketplace.
