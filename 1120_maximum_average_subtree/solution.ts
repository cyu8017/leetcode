// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function maximumAverageSubtree(root: TreeNode | null): number {
    let best = 0;
    const dfs = (node) => {
        if (!node) return [0, 0];
        const [ls, lc] = dfs(node.left);
        const [rs, rc] = dfs(node.right);
        const totalSum = ls + rs + node.val;
        const totalCount = lc + rc + 1;
        best = Math.max(best, totalSum / totalCount);
        return [totalSum, totalCount];
    };
    dfs(root);
    return best;
}
