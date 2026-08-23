// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number[]} queries
 * @return {number[]}
 */
var treeQueries = function(root, queries) {
    const height = new Map(), level = new Map(), levelMax = new Map();
    const dfs = (node, d) => {
        if (!node) return -1;
        level.set(node.val, d);
        const h = 1 + Math.max(dfs(node.left, d + 1), dfs(node.right, d + 1));
        height.set(node.val, h);
        let arr = levelMax.get(d);
        if (!arr) {
            arr = [];
            levelMax.set(d, arr);
        }
        if (!arr.length) arr.push(h);
        else if (h >= arr[0]) {
            if (arr.length === 1) arr.push(arr[0]);
            else arr[1] = arr[0];
            arr[0] = h;
        } else if (arr.length === 1 || h > arr[1]) {
            if (arr.length === 1) arr.push(h);
            else arr[1] = h;
        }
        return h;
    };
    dfs(root, 0);
    const ans = Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        const d = level.get(q), h = height.get(q);
        const top = levelMax.get(d);
        if (top[0] === h) {
            if (top.length > 1) ans[i] = d + top[1];
            else ans[i] = d - 1;
        } else {
            ans[i] = d + top[0];
        }
    }
    return ans;
};
