// LeetCode 0508 - Most Frequent Subtree Sum
// https://leetcode.com/problems/most-frequent-subtree-sum/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    findFrequentTreeSum(root) {
        const counts = new Map();
        const subtreeSum = (node) => {
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

module.exports = { Solution, TreeNode };
