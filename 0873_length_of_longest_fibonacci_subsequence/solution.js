// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    const n = arr.length;
    const index = new Map();
    for (let i = 0; i < n; i++) index.set(arr[i], i);
    const dp = Array.from({ length: n }, () => new Array(n).fill(2));
    let ans = 0;
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < j; i++) {
            const k = index.get(arr[j] - arr[i]);
            if (k !== undefined && k < i) {
                dp[i][j] = dp[k][i] + 1;
                ans = Math.max(ans, dp[i][j]);
            }
        }
    }
    return ans >= 3 ? ans : 0;
};
