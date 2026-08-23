// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} target
 * @param {number} k
 * @return {number[]}
 */
var distanceK = function(root, target, k) {
    const graph = new Map();
    const add = (a, b) => {
        if (!graph.has(a)) graph.set(a, []);
        graph.get(a).push(b);
    };
    const build = (node, parent) => {
        if (!node) return;
        if (parent) {
            add(node, parent);
            add(parent, node);
        }
        build(node.left, node);
        build(node.right, node);
    };
    build(root, null);
    const queue = [target];
    const seen = new Set([target]);
    let dist = 0;
    while (queue.length) {
        if (dist === k) return queue.map(node => node.val);
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            const node = queue.shift();
            for (const nei of (graph.get(node) || [])) {
                if (!seen.has(nei)) {
                    seen.add(nei);
                    queue.push(nei);
                }
            }
        }
        dist++;
    }
    return [];
};
