// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
    const stack = [];
    const m = part.length;
    for (const ch of s) {
        stack.push(ch);
        if (stack.length >= m && stack.slice(-m).join("") === part) stack.length -= m;
    }
    return stack.join("");
};
