// LeetCode 0132 - Palindrome Partitioning II
// https://leetcode.com/problems/palindrome-partitioning-ii/

/**
 * @param {string} s
 * @return {number}
 */
var minCut = function(s) {
    const n = s.length;
    if (n === 0) return 0;

    const isPalindrome = Array.from({ length: n }, () => Array(n).fill(false));
    for (let start = n - 1; start >= 0; start -= 1) {
        for (let end = start; end < n; end += 1) {
            if (s[start] === s[end] && (end - start < 2 || isPalindrome[start + 1][end - 1])) {
                isPalindrome[start][end] = true;
            }
        }
    }

    const cuts = Array.from({ length: n }, (_, index) => index);
    for (let end = 0; end < n; end += 1) {
        if (isPalindrome[0][end]) {
            cuts[end] = 0;
            continue;
        }
        for (let start = 0; start < end; start += 1) {
            if (isPalindrome[start + 1][end]) {
                cuts[end] = Math.min(cuts[end], cuts[start] + 1);
            }
        }
    }
    return cuts[n - 1];
};