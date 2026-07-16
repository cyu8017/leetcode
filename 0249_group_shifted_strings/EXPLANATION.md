# How We Solve Group Shifted Strings

Strings in the same shift group share the same relative letter offsets.

## Steps

1. For each string, compute offsets from its first character mod 26.
2. Use that offset tuple as the group key.
3. Append the string to the bucket for its key.
4. Collect all buckets as groups.
5. Return the grouped lists.
