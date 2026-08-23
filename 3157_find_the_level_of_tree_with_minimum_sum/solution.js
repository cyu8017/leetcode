// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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
 * @return {number}
 */
var minimumLevel = function(root) {
    const q = [root];
    let s = Number.MAX_SAFE_INTEGER;
    let ans = 0;
    for (let level = 1; q.length; level++) {
        let t = 0;
        let m = q.length;
        while (m-- > 0) {
            const node = q.shift();
            t += node.val;
            if (node.left !== null) q.push(node.left);
            if (node.right !== null) q.push(node.right);
        }
        if (s > t) {
            s = t;
            ans = level;
        }
    }
    return ans;
};
