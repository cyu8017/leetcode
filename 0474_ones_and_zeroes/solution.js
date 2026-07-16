// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

class Solution {
    findMaxForm(strs, m, n) {
        const dp = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
        for (const string of strs) {
            const zeros = (string.match(/0/g) || []).length;
            const ones = string.length - zeros;
            for (let zero = m; zero >= zeros; zero -= 1) {
                for (let one = n; one >= ones; one -= 1) {
                    dp[zero][one] = Math.max(dp[zero][one], dp[zero - zeros][one - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }
}

module.exports = { Solution };
