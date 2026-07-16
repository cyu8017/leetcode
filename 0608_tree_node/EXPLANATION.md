# How We Solve Tree Node

Classify each node as Root, Inner, or Leaf from parent links.

## Steps

1. `p_id IS NULL` means Root.
2. Ids that appear as some other row's `p_id` are Inner.
3. Everything else is a Leaf.
