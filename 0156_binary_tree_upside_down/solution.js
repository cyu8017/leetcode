// LeetCode 0156 - Binary Tree Upside Down
// https://leetcode.com/problems/binary-tree-upside-down/

/**
 * Flips a binary tree along its left spine.
 * @param {TreeNode|null} root
 * @return {TreeNode|null}
 */
var upsideDownBinaryTree = function(root) {
    let previous = null;
    let previousRight = null;
    let current = root;

    while (current !== null) {
        const next = current.left;
        current.left = previousRight;
        previousRight = current.right;
        current.right = previous;
        previous = current;
        current = next;
    }

    return previous;
};