// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

/**
 * @param {number[]} preorder
 * @return {boolean}
 */
var verifyPreorder = function(preorder) {
    let low = Number.NEGATIVE_INFINITY;
    const stack = [];

    for (const value of preorder) {
        if (value < low) {
            return false;
        }
        while (stack.length > 0 && stack[stack.length - 1] < value) {
            low = stack.pop();
        }
        stack.push(value);
    }

    return true;
};
