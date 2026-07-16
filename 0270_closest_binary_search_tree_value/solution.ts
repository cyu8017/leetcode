// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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

function closestValue(root: TreeNode | null, target: number): number {
    let closest = root!.val;
    let current: TreeNode | null = root;
    while (current) {
        if (Math.abs(closest - target) > Math.abs(current.val - target)) {
            closest = current.val;
        }
        if (current.val === target) {
            return current.val;
        }
        current = target < current.val ? current.left : current.right;
    }
    return closest;
}
