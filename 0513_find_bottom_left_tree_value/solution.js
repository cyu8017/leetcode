// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    findBottomLeftValue(root) {
        const queue = [root];
        let leftmost = root.val;
        while (queue.length) {
            const levelSize = queue.length;
            for (let index = 0; index < levelSize; index += 1) {
                const node = queue.shift();
                if (index === 0) leftmost = node.val;
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
        }
        return leftmost;
    }
}

module.exports = { Solution, TreeNode };
