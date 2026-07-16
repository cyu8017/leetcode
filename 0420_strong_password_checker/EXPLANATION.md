# How We Solve Strong Password Checker

Greedy edits combine length fixes, type fixes, and repeat replacements.

## Steps

1. Count missing character classes and triple-repeat replacements.
2. Insert characters when length is below six.
3. When too long, use deletions to reduce needed replacements and add missing types.
