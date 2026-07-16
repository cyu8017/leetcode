// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export class Solution {
    treeToDoublyList(root: TreeNode | null): TreeNode | null {
        if (!root) return null;

        let first: TreeNode | null = null;
        let last: TreeNode | null = null;

        const inorder = (node: TreeNode | null): void => {
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
