// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isCompleteTree = function(root) {
    const q = [root];
    let end = false;
    while (q.length) {
        const node = q.shift();
        if (node === null) end = true;
        else {
            if (end) return false;
            q.push(node.left);
            q.push(node.right);
        }
    }
    return true;
};
