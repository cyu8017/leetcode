// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

/**
 * @param {number[][]} questions
 * @return {number}
 */
var mostPoints = function(questions) {
    const n = questions.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        const pts = questions[i][0], brain = questions[i][1];
        const next = i + brain + 1;
        const take = pts + (next < n ? dp[next] : 0);
        dp[i] = Math.max(dp[i + 1], take);
    }
    return dp[0];
};
