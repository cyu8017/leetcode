// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

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

export function findClosestLeaf(root: TreeNode | null, k: number): number {
    const graph = new Map();
    const leaves = new Set();
    const build = (node, parent) => {
        if (node === null) return;
        if (!graph.has(node.val)) graph.set(node.val, []);
        if (parent !== null) {
            if (!graph.has(parent.val)) graph.set(parent.val, []);
            graph.get(node.val).push(parent.val);
            graph.get(parent.val).push(node.val);
        }
        if (node.left === null && node.right === null) leaves.add(node.val);
        build(node.right, node);
        build(node.left, node);
    };
    build(root, null);
    const q = [k];
    const seen = new Set([k]);
    while (q.length > 0) {
        const value = q.shift();
        if (leaves.has(value)) return value;
        if (!graph.has(value)) continue;
        for (const neighbor of graph.get(value)) {
            if (!seen.has(neighbor)) {
                seen.add(neighbor);
                q.push(neighbor);
            }
        }
    }
    return -1;
}
