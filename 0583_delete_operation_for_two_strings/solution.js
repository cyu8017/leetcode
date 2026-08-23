// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    const m = word1.length, n = word2.length;
    let prev = Array(n + 1).fill(0);
    let curr = Array(n + 1).fill(0);
    for (let i = 1; i <= m; ++i) {
        for (let j = 1; j <= n; ++j) {
            if (word1[i - 1] === word2[j - 1]) curr[j] = prev[j - 1] + 1;
            else curr[j] = Math.max(prev[j], curr[j - 1]);
        }
        [prev, curr] = [curr, prev];
        curr.fill(0);
    }
    return m + n - 2 * prev[n];
};
