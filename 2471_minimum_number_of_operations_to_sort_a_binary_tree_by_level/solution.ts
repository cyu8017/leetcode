// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

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

export function minimumOperations(root: TreeNode | null): number {
    if (!root) return 0;
    let ans = 0;
    const q = [root];
    while (q.length) {
        const sz = q.length;
        const vals = Array(sz);
        for (let i = 0; i < sz; i++) {
            const node = q.shift();
            vals[i] = node.val;
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        const sorted = vals.slice().sort((a, b) => a - b);
        const pos = new Map();
        for (let i = 0; i < sz; i++) pos.set(vals[i], i);
        for (let i = 0; i < sz; i++) {
            if (vals[i] !== sorted[i]) {
                const j = pos.get(sorted[i]);
                [vals[i], vals[j]] = [vals[j], vals[i]];
                pos.set(vals[j], j);
                pos.set(vals[i], i);
                ans++;
            }
        }
    }
    return ans;
}
