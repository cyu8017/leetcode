// LeetCode 0965 - Univalued Binary Tree
// https://leetcode.com/problems/univalued-binary-tree/

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

function TreeNode(val: any, left: any, right: any): any {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}
export function isUnivalTree(root: TreeNode | null): boolean {
    if (!root) return true;
    const dfs = (node, v) => {
        if (!node) return true;
        if (node.val !== v) return false;
        return dfs(node.left, v) && dfs(node.right, v);
    };
    return dfs(root, root.val);
}
