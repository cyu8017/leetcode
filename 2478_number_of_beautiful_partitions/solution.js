// LeetCode 2478 - Number of Beautiful Partitions
// https://leetcode.com/problems/number-of-beautiful-partitions/

/**
 * @param {string} s
 * @param {number} k
 * @param {number} minLength
 * @return {number}
 */
var beautifulPartitions = function(s, k, minLength) {
    const mod = 1000000007;
    const isPrime = (c) => c === '2' || c === '3' || c === '5' || c === '7';
    const n = s.length;
    if (!isPrime(s[0]) || isPrime(s[n - 1])) return 0;
    const dp = Array.from({ length: k + 1 }, () => Array(n + 1).fill(0));
    dp[0][0] = 1;
    for (let p = 1; p <= k; p++) {
        let pref = 0, j = 0;
        for (let i = 1; i <= n; i++) {
            while (j <= i - minLength) {
                if (j === 0 || (isPrime(s[j]) && !isPrime(s[j - 1]))) {
                    pref = (pref + dp[p - 1][j]) % mod;
                }
                j++;
            }
            if (!isPrime(s[i - 1])) dp[p][i] = pref;
        }
    }
    return dp[k][n];
};
