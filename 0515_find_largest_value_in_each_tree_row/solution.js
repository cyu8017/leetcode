// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    largestValues(root) {
        if (!root) return [];
        const result = [];
        const queue = [root];
        while (queue.length) {
            let levelMax = -Infinity;
            for (let count = queue.length; count > 0; count -= 1) {
                const node = queue.shift();
                levelMax = Math.max(levelMax, node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            result.push(levelMax);
        }
        return result;
    }
}

module.exports = { Solution, TreeNode };
