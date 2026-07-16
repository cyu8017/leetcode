// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node {
    constructor(val = null, children = null) {
        this.val = val;
        this.children = children ?? [];
    }
}

class Solution {
    levelOrder(root) {
        if (!root) return [];

        const result = [];
        const queue = [root];

        while (queue.length > 0) {
            const level = [];
            const size = queue.length;
            for (let i = 0; i < size; i += 1) {
                const node = queue.shift();
                level.push(node.val);
                queue.push(...node.children);
            }
            result.push(level);
        }

        return result;
    }
}

module.exports = { Solution, Node };
