// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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

export function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    if (root === null) return new TreeNode(val);
    let node = root;
    while (true) {
        if (val < node.val) {
            if (node.left === null) { node.left = new TreeNode(val); break; }
            node = node.left;
        } else {
            if (node.right === null) { node.right = new TreeNode(val); break; }
            node = node.right;
        }
    }
    return root;
}
