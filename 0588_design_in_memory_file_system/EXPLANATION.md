# How We Solve Design In-Memory File System

Represent the tree with nested dictionaries for directories and strings for file contents.

## Steps

1. `mkdir` walks path parts and creates missing directory dicts.
2. `addContentToFile` creates or appends a string leaf.
3. `ls` returns a single file name or the sorted directory children; `readContentFromFile` returns the string.
