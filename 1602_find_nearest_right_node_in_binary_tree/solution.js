// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

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
 * @param {TreeNode|number} u
 * @return {TreeNode|null}
 */
var findNearestRightNode = function(root, u) {
    const asNode = u && typeof u === "object" && "val" in u;
    const target = asNode ? u.val : u;
    let q = root ? [root] : [];
    while (q.length) {
        const nxt = [];
        for (let i = 0; i < q.length; i++) {
            const node = q[i];
            if (node.val === target) {
                const ans = i + 1 < q.length ? q[i + 1] : null;
                return asNode ? ans : (ans ? ans.val : null);
            }
            if (node.left) nxt.push(node.left);
            if (node.right) nxt.push(node.right);
        }
        q = nxt;
    }
    return null;
};
