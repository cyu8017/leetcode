// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

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
    deleteNode(root: TreeNode | null, key: number): TreeNode | null {
        if (!root) return null;
        if (key < root.val) {
            root.left = this.deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = this.deleteNode(root.right, key);
        } else {
            if (!root.left) return root.right;
            if (!root.right) return root.left;
            let successor = root.right;
            while (successor.left) {
                successor = successor.left;
            }
            root.val = successor.val;
            root.right = this.deleteNode(root.right, successor.val);
        }
        return root;
    }
}
