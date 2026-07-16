// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

class Solution {
    deleteNode(root, key) {
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

module.exports = { Solution };
