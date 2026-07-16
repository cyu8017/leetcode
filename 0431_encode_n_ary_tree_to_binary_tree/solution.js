"use strict";
// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Solution = exports.TreeNode = exports.Node = void 0;
class Node {
    constructor(val = null, children = null) {
        this.val = val;
        this.children = children ?? [];
    }
}
exports.Node = Node;
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
exports.TreeNode = TreeNode;
class Solution {
    encodeNaryTree(root) {
        if (!root)
            return null;
        const binary = new TreeNode(root.val);
        if (!root.children.length)
            return binary;
        binary.left = this.encodeNaryTree(root.children[0]);
        let sibling = binary.left;
        for (let i = 1; i < root.children.length; i += 1) {
            sibling.right = this.encodeNaryTree(root.children[i]);
            sibling = sibling.right;
        }
        return binary;
    }
    decodeBinaryTree(root) {
        if (!root)
            return null;
        const node = new Node(root.val, []);
        let current = root.left;
        while (current) {
            node.children.push(this.decodeBinaryTree(current));
            current = current.right;
        }
        return node;
    }
}
exports.Solution = Solution;
