// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

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
    boundaryOfBinaryTree(root: TreeNode | null): number[] {
        if (!root) return [];

        const isLeaf = (node: TreeNode | null): boolean =>
            node !== null && node.left === null && node.right === null;

        const leftBoundary = (node: TreeNode | null): number[] => {
            if (!node || isLeaf(node)) return [];
            if (node.left) return [node.val, ...leftBoundary(node.left)];
            return [node.val, ...leftBoundary(node.right)];
        };

        const rightBoundary = (node: TreeNode | null): number[] => {
            if (!node || isLeaf(node)) return [];
            if (node.right) return [...rightBoundary(node.right), node.val];
            return [...rightBoundary(node.left), node.val];
        };

        const leaves = (node: TreeNode | null): number[] => {
            if (!node) return [];
            if (isLeaf(node)) return [node.val];
            return [...leaves(node.left), ...leaves(node.right)];
        };

        if (isLeaf(root)) return [root.val];
        return [root.val, ...leftBoundary(root.left), ...leaves(root), ...rightBoundary(root.right)];
    }
}
