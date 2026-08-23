// LeetCode 0538 - Convert BST to Greater Tree
// https://leetcode.com/problems/convert-bst-to-greater-tree/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    convertBST(root) {
        let running = 0;
        const reverseInorder = (node) => {
            if (!node) return;
            reverseInorder(node.right);
            running += node.val;
            node.val = running;
            reverseInorder(node.left);
        };
        reverseInorder(root);
    }
}

module.exports = { Solution, TreeNode };
