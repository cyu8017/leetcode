// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export class Solution {
    pathSum(root: TreeNode | null, targetSum: number): number {
        const prefixCounts = new Map<number, number>([[0, 1]]);

        const dfs = (node: TreeNode | null, current: number): number => {
            if (!node) return 0;
            current += node.val;
            let total = prefixCounts.get(current - targetSum) ?? 0;
            prefixCounts.set(current, (prefixCounts.get(current) ?? 0) + 1);
            total += dfs(node.left, current);
            total += dfs(node.right, current);
            prefixCounts.set(current, prefixCounts.get(current)! - 1);
            return total;
        };

        return dfs(root, 0);
    }
}
