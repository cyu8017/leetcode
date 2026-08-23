// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s) {
    const lastIndex = {};
    for (let index = 0; index < s.length; index += 1) {
        lastIndex[s[index]] = index;
    }
    const stack = [];
    const seen = new Set();
    for (let index = 0; index < s.length; index += 1) {
        const char = s[index];
        if (seen.has(char)) {
            continue;
        }
        while (stack.length > 0 && stack[stack.length - 1] > char && lastIndex[stack[stack.length - 1]] > index) {
            seen.delete(stack.pop());
        }
        stack.push(char);
        seen.add(char);
    }
    return stack.join("");
};
