// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export class Solution {
    convertBST(root: TreeNode | null): void {
        let running = 0;
        const reverseInorder = (node: TreeNode | null): void => {
            if (!node) return;
            reverseInorder(node.right);
            running += node.val;
            node.val = running;
            reverseInorder(node.left);
        };
        reverseInorder(root);
    }
}
