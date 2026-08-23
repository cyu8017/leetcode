// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class Solution {
    treeToDoublyList(root) {
        if (!root) return null;

        let first = null;
        let last = null;

        const inorder = (node) => {
            if (!node) return;
            inorder(node.left);
            if (last) {
                last.right = node;
                node.left = last;
            } else {
                first = node;
            }
            last = node;
            inorder(node.right);
        };

        inorder(root);
        if (first && last) {
            first.left = last;
            last.right = first;
        }
        return first;
    }
}

module.exports = { Solution };
