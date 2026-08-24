// LeetCode 2196 - Create Binary Tree From Descriptions
// https://leetcode.com/problems/create-binary-tree-from-descriptions/

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

export function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const nodes = new Map();
    const child = new Set();
    for (const [p, c, isLeft] of descriptions) {
        if (!nodes.has(p)) nodes.set(p, new TreeNode(p));
        if (!nodes.has(c)) nodes.set(c, new TreeNode(c));
        if (isLeft === 1) nodes.get(p).left = nodes.get(c);
        else nodes.get(p).right = nodes.get(c);
        child.add(c);
    }
    for (const [k, v] of nodes)
        if (!child.has(k)) return v;
    return null;
}
