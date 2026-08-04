// LeetCode 1335 - Minimum Difficulty Of A Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
var minDifficulty = function(jobDifficulty, d) {
    const n = jobDifficulty.length;
    if (n < d) return -1;
    let dp = Array(n).fill(1e9);
    let hardest = 0;
    for (let i = 0; i < n; i++) {
        hardest = Math.max(hardest, jobDifficulty[i]);
        dp[i] = hardest;
    }
    for (let day = 1; day < d; day++) {
        const nxt = Array(n).fill(1e9);
        for (let end = day; end < n; end++) {
            hardest = 0;
            for (let start = end; start >= day; start--) {
                hardest = Math.max(hardest, jobDifficulty[start]);
                nxt[end] = Math.min(nxt[end], dp[start - 1] + hardest);
            }
        }
        dp = nxt;
    }
    return dp[n - 1];
};
