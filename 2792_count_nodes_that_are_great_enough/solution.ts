// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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

export function countGreatEnoughNodes(root: TreeNode | null, k: number): number {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [];
        const vals = [node.val, ...dfs(node.left), ...dfs(node.right)];
        let smaller = 0;
        for (const v of vals) if (v < node.val) smaller++;
        if (smaller >= k) ans++;
        return vals;
    };
    dfs(root);
    return ans;
}
