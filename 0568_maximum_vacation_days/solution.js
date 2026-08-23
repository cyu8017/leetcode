// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

/**
 * @param {number[][]} flights
 * @param {number[][]} days
 * @return {number}
 */
var maxVacationDays = function(flights, days) {
    const cities = flights.length;
    const weeks = days[0].length;
    const NEG = -1000000000;
    let dp = Array(cities).fill(NEG);
    dp[0] = 0;
    for (let week = 0; week < weeks; ++week) {
        const nxt = Array(cities).fill(NEG);
        for (let city = 0; city < cities; ++city) {
            if (dp[city] === NEG) continue;
            for (let dest = 0; dest < cities; ++dest) {
                if (dest === city || flights[city][dest] === 1) {
                    nxt[dest] = Math.max(nxt[dest], dp[city] + days[dest][week]);
                }
            }
        }
        dp = nxt;
    }
    let best = NEG;
    for (const v of dp) best = Math.max(best, v);
    return best;
};
