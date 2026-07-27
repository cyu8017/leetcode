// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    const players = ages.map((age, i) => [age, scores[i]]).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    const dp = Array(players.length).fill(0);
    for (let i = 0; i < players.length; i++) {
        const score = players[i][1];
        let best = 0;
        for (let j = 0; j < i; j++) if (players[j][1] <= score) best = Math.max(best, dp[j]);
        dp[i] = score + best;
    }
    return Math.max(0, ...dp);
};
