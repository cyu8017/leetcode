// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function(s) {
    const stack = [];
    for (const ch of s) {
        if (stack.length && stack[stack.length - 1] !== ch &&
            stack[stack.length - 1].toLowerCase() === ch.toLowerCase()) {
            stack.pop();
        } else {
            stack.push(ch);
        }
    }
    return stack.join("");
};
