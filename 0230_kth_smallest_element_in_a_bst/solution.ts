// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function kthSmallest(root: TreeNode | null, k: number): number {
    const stack: TreeNode[] = [];
    let current: TreeNode | null = root;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop()!;
        k -= 1;
        if (k === 0) {
            return current.val;
        }
        current = current.right;
    }

    return -1;
}
