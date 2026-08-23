// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let x = 0;
    for (const op of operations) {
        if (op[1] === '+') x++;
        else x--;
    }
    return x;
};
