# How We Solve Subtree of Another Tree

Check every node of `root` for an identical match with `subRoot`.

## Steps

1. Define an equality helper that compares structure and values recursively.
2. At each node, test whether the subtree rooted there equals `subRoot`.
3. Otherwise recurse into the left and right children.
