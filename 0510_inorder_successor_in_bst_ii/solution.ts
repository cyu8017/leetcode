// LeetCode 0510 - Inorder Successor in BST II
// https://leetcode.com/problems/inorder-successor-in-bst-ii/

export class Node {
    val: number;
    left: Node | null;
    right: Node | null;
    parent: Node | null;

    constructor(val = 0, left: Node | null = null, right: Node | null = null, parent: Node | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
        this.parent = parent;
    }
}

export class Solution {
    inorderSuccessor(node: Node): Node | null {
        if (node.right) {
            let current: Node = node.right;
            while (current.left) current = current.left;
            return current;
        }
        let current: Node | null = node;
        while (current.parent && current === current.parent.right) {
            current = current.parent;
        }
        return current.parent;
    }
}
