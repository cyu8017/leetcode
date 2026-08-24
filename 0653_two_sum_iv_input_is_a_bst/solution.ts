// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

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

export function findTarget(root: TreeNode | null, k: number): boolean {
    const seen = new Set();
    const dfs = (node) => {
        if (node == null) return false;
        if (seen.has(k - node.val)) return true;
        seen.add(node.val);
        return dfs(node.left) || dfs(node.right);
    };
    return dfs(root);
}
