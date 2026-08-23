// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    findMode(root) {
        const counts = new Map();
        let best = 0;
        const inorder = (node) => {
            if (!node) return;
            inorder(node.left);
            counts.set(node.val, (counts.get(node.val) || 0) + 1);
            best = Math.max(best, counts.get(node.val));
            inorder(node.right);
        };
        inorder(root);
        return [...counts.entries()].filter(([, count]) => count === best).map(([value]) => value);
    }
}

module.exports = { Solution, TreeNode };
