# How We Solve Closest Binary Search Tree Value II

Collect sorted values, then expand outward from the insertion point.

## Steps

1. Inorder traverse the BST into a sorted list.
2. Find the first value not less than the target.
3. Repeatedly pick the closer side between left and right neighbors.
4. Append that value and move the pointer inward.
5. Stop after collecting k values.
