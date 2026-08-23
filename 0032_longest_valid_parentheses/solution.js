// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    const stack = [-1];
    let best = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === "(") {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i);
            } else {
                best = Math.max(best, i - stack[stack.length - 1]);
            }
        }
    }

    return best;
};
