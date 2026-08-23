// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const stack = [];
    const pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    };

    for (const ch of s) {
        if (ch === "(" || ch === "[" || ch === "{") {
            stack.push(ch);
        } else if (stack.length === 0 || stack.pop() !== pairs[ch]) {
            return false;
        }
    }

    return stack.length === 0;
};
