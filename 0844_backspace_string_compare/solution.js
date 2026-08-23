// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {
    const build = (text) => {
        const stack = [];
        for (const ch of text) {
            if (ch === '#') {
                if (stack.length) stack.pop();
            } else {
                stack.push(ch);
            }
        }
        return stack.join('');
    };
    return build(s) === build(t);
};
