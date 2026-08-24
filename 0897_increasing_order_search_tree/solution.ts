// LeetCode 0897 - Increasing Order Search Tree
// https://leetcode.com/problems/increasing-order-search-tree/

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
export function increasingBST(root: TreeNode | null): TreeNode | null {
    const dummy = new TreeNode(0);
    let cur = dummy;
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        node.left = null;
        cur.right = node;
        cur = node;
        inorder(node.right);
    };
    inorder(root);
    return dummy.right;
}
