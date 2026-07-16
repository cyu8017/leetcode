// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Node {
    constructor(val = 0, left = null, right = null, parent = null) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }
}

class Solution {
    inorderSuccessor(node) {
        if (node.right) {
            let current = node.right;
            while (current.left) current = current.left;
            return current;
        }
        let current = node;
        while (current.parent && current === current.parent.right) {
            current = current.parent;
        }
        return current.parent;
    }
}

module.exports = { Solution, Node };
