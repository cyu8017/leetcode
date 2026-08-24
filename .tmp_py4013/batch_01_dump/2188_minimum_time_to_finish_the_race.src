// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

/**
 * @param {number[][]} tires
 * @param {number} changeTime
 * @param {number} numLaps
 * @return {number}
 */
var minimumFinishTime = function(tires, changeTime, numLaps) {
    const INF = 1 << 30;
    const minTime = new Array(20).fill(INF);
    for (const tire of tires) {
        const f = tire[0], r = tire[1];
        let t = f, lap = f;
        for (let x = 1; x < 20 && t < minTime[x]; x++) {
            minTime[x] = t;
            lap *= r;
            if (lap > changeTime + f) break;
            t += lap;
        }
    }
    const dp = new Array(numLaps + 1).fill(INF);
    dp[0] = -changeTime;
    for (let i = 1; i <= numLaps; i++)
        for (let j = 1; j <= i && j < 20; j++)
            dp[i] = Math.min(dp[i], dp[i - j] + changeTime + minTime[j]);
    return dp[numLaps];
};
