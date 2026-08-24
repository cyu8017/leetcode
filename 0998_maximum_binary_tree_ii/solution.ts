// LeetCode 0998 - Maximum Binary Tree II
// https://leetcode.com/problems/maximum-binary-tree-ii/

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

export function insertIntoMaxTree(root: TreeNode | null, val: number): TreeNode | null {
    if (!root || val > root.val) {
        const node = new TreeNode(val);
        node.left = root;
        return node;
    }
    root.right = insertIntoMaxTree(root.right, val);
    return root;
}
