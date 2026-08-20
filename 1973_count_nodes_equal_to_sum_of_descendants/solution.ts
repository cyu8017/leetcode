// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

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

function equalToDescendants(root: TreeNode | null): number {
    let ans = 0;
    const dfs = (node: TreeNode | null): number => {
        if (!node) return 0;
        const total = dfs(node.left) + dfs(node.right);
        if (total === node.val) ans++;
        return total + node.val;
    };
    dfs(root);
    return ans;
}
