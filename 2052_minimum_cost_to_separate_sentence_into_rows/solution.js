// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

/**
 * @param {string} sentence
 * @param {number} k
 * @return {number}
 */
var minimumCost = function(sentence, k) {
    const words = sentence.trim().split(/\s+/);
    const n = words.length;
    const INF = 1e18;
    const dp = new Array(n + 1).fill(INF);
    dp[n] = 0;
    for (let i = n - 1; i >= 0; i--) {
        let length = -1;
        for (let j = i; j < n; j++) {
            length += 1 + words[j].length;
            if (length > k) break;
            let cost = 0;
            if (j < n - 1) {
                const extra = k - length;
                cost = extra * extra;
            }
            dp[i] = Math.min(dp[i], cost + dp[j + 1]);
        }
    }
    return dp[0];
};
