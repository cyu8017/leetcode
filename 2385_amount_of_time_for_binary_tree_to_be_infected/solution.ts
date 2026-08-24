// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

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

export function amountOfTime(root: TreeNode | null, start: number): number {
    const g = new Map();
    const build = (node, parent) => {
        if (!node) return;
        if (parent) {
            if (!g.has(node.val)) g.set(node.val, []);
            if (!g.has(parent.val)) g.set(parent.val, []);
            g.get(node.val).push(parent.val);
            g.get(parent.val).push(node.val);
        }
        build(node.left, node);
        build(node.right, node);
    };
    build(root, null);
    let ans = 0;
    const vis = new Set([start]);
    const q = [[start, 0]];
    while (q.length > 0) {
        const [cur, d] = q.shift();
        ans = Math.max(ans, d);
        for (const nxt of (g.get(cur) || [])) {
            if (!vis.has(nxt)) {
                vis.add(nxt);
                q.push([nxt, d + 1]);
            }
        }
    }
    return ans;
}
