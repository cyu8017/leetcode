// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function maxAncestorDiff(root: TreeNode | null): number {
    if (!root) return 0;
    const dfs = (node: TreeNode | null, lo: number, hi: number): number => {
        if (!node) return hi - lo;
        lo = Math.min(lo, node.val);
        hi = Math.max(hi, node.val);
        return Math.max(dfs(node.left, lo, hi), dfs(node.right, lo, hi));
    };
    return dfs(root, root.val, root.val);
}
