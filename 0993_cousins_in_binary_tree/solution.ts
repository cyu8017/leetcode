// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

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

export function isCousins(root: TreeNode | null, x: number, y: number): boolean {
    const depth = new Map();
    const parent = new Map();
    const dfs = (node, p, d) => {
        if (!node) return;
        depth.set(node.val, d);
        parent.set(node.val, p);
        dfs(node.left, node, d + 1);
        dfs(node.right, node, d + 1);
    };
    dfs(root, null, 0);
    return depth.get(x) === depth.get(y) && parent.get(x) !== parent.get(y);
}
