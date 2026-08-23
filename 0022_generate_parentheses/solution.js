// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];

    function backtrack(path, openCount, closeCount) {
        if (path.length === 2 * n) {
            result.push(path.join(""));
            return;
        }
        if (openCount < n) {
            path.push("(");
            backtrack(path, openCount + 1, closeCount);
            path.pop();
        }
        if (closeCount < openCount) {
            path.push(")");
            backtrack(path, openCount, closeCount + 1);
            path.pop();
        }
    }

    backtrack([], 0, 0);
    return result;
};
