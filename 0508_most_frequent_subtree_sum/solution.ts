// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

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
    findFrequentTreeSum(root: TreeNode | null): number[] {
        const counts = new Map<number, number>();
        const subtreeSum = (node: TreeNode | null): number => {
            if (!node) return 0;
            const total = node.val + subtreeSum(node.left) + subtreeSum(node.right);
            counts.set(total, (counts.get(total) || 0) + 1);
            return total;
        };
        subtreeSum(root);
        if (!counts.size) return [];
        const best = Math.max(...counts.values());
        return [...counts.entries()].filter(([, count]) => count === best).map(([value]) => value).sort((a, b) => a - b);
    }
}
