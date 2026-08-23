// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @param {number} p
 * @param {number} q
 * @return {number}
 */
var findDistance = function(root, p, q) {
    const graph = new Map();
    const dfs = (node, parent) => {
        if (!node) {
            return;
        }
        if (!graph.has(node.val)) {
            graph.set(node.val, []);
        }
        if (parent) {
            graph.get(node.val).push(parent.val);
            graph.get(parent.val).push(node.val);
        }
        dfs(node.left, node);
        dfs(node.right, node);
    };
    dfs(root, null);
    const queue = [[p, 0]];
    const seen = new Set([p]);
    while (queue.length > 0) {
        const [node, dist] = queue.shift();
        if (node === q) {
            return dist;
        }
        for (const nei of graph.get(node)) {
            if (!seen.has(nei)) {
                seen.add(nei);
                queue.push([nei, dist + 1]);
            }
        }
    }
    return -1;
};
