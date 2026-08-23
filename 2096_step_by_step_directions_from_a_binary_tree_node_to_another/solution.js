// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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
 * @param {number} startValue
 * @param {number} destValue
 * @return {string}
 */
var getDirections = function(root, startValue, destValue) {
    const path = (node, target, p) => {
        if (node === null) return false;
        if (node.val === target) return true;
        p.push('L');
        if (path(node.left, target, p)) return true;
        p[p.length - 1] = 'R';
        if (path(node.right, target, p)) return true;
        p.pop();
        return false;
    };
    const ps = [], pd = [];
    path(root, startValue, ps);
    path(root, destValue, pd);
    let i = 0;
    while (i < ps.length && i < pd.length && ps[i] === pd[i]) i++;
    return 'U'.repeat(ps.length - i) + pd.slice(i).join('');
};
