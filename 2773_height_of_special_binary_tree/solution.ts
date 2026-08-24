// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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

export function heightOfTree(root: TreeNode | null): number {
    if (!root) return -1;
    const dfs = (node) => {
        if (!node) return -1;
        if (node.left && node.left.right === node) return dfs(node.right) + 1;
        if (node.right && node.right.left === node) return dfs(node.left) + 1;
        return Math.max(dfs(node.left), dfs(node.right)) + 1;
    };
    return dfs(root);
}
