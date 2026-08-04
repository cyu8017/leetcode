// LeetCode 1315 - Sum Of Nodes With Even Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumEvenGrandparent = function(root) {
    const dfs = (node, parent, grandparent) => {
        if (!node) return 0;
        const add = grandparent && grandparent.val % 2 === 0 ? node.val : 0;
        return add + dfs(node.left, node, parent) + dfs(node.right, node, parent);
    };
    return dfs(root, null, null);
};
