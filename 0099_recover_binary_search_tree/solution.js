// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {void}
 */
var recoverTree = function(root) {
    let first = null;
    let second = null;
    let previous = null;
    const stack = [];
    let current = root;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop();
        if (previous && previous.val > current.val) {
            if (first === null) {
                first = previous;
            }
            second = current;
        }
        previous = current;
        current = current.right;
    }

    if (first && second) {
        const temp = first.val;
        first.val = second.val;
        second.val = temp;
    }
};
