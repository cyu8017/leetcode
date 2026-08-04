// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

/**
 * @param {string} text
 * @return {number}
 */
var longestDecomposition = function(text) {
    const n = text.length;
    let ans = 0, i = 0;
    while (i < n - i) {
        let found = false;
        for (let length = 1; length <= Math.floor((n - 2 * i) / 2); length++) {
            if (text.slice(i, i + length) === text.slice(n - i - length, n - i)) {
                ans += 2;
                i += length;
                found = true;
                break;
            }
        }
        if (!found) {
            ans++;
            break;
        }
    }
    return ans;
};
