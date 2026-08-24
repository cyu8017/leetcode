// LeetCode 2583 - Kth Largest Sum in a Binary Tree
// https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

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

export function kthLargestLevelSum(root: TreeNode | null, k: number): number {
    if (!root) return -1;
    const sums = [];
    const q = [root];
    while (q.length) {
        const sz = q.length;
        let s = 0;
        for (let i = 0; i < sz; ++i) {
            const node = q.shift();
            s += node.val;
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        sums.push(s);
    }
    sums.sort((a, b) => b - a);
    if (k > sums.length) return -1;
    return sums[k - 1];
}
