// LeetCode 0655 - Print Binary Tree
// https://leetcode.com/problems/print-binary-tree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function printTree(root: TreeNode | null): string[][] {
    const height = (node) => node == null ? -1 : 1 + Math.max(height(node.left), height(node.right));
    const h = height(root);
    const rows = h + 1;
    const cols = (1 << (h + 1)) - 1;
    const res = Array.from({ length: rows }, () => Array(cols).fill(""));
    const place = (node, r, c) => {
        if (node == null) return;
        res[r][c] = String(node.val);
        if (r === h) return;
        const offset = 1 << (h - r - 1);
        place(node.left, r + 1, c - offset);
        place(node.right, r + 1, c + offset);
    };
    place(root, 0, Math.floor((cols - 1) / 2));
    return res;
}
