// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

/**
 * @param {string} s
 * @return {string}
 */
var shortestPalindrome = function(s) {
    if (!s) {
        return "";
    }
    const reversed = [...s].reverse().join("");
    const combined = `${s}#${reversed}`;
    const pi = new Array(combined.length).fill(0);
    let lps = 0;
    for (let i = 1; i < combined.length; i += 1) {
        while (lps && combined[i] !== combined[lps]) {
            lps = pi[lps - 1];
        }
        if (combined[i] === combined[lps]) {
            lps += 1;
        }
        pi[i] = lps;
    }
    const prefixLen = pi[combined.length - 1];
    return reversed.slice(0, s.length - prefixLen) + s;
};
