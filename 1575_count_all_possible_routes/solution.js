// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

/**
 * @param {number[]} locations
 * @param {number} start
 * @param {number} finish
 * @param {number} fuel
 * @return {number}
 */
var countRoutes = function(locations, start, finish, fuel) {
    const MOD = 1000000007;
    const memo = new Map();
    const dp = (city, left) => {
        const key = city + "," + left;
        if (memo.has(key)) return memo.get(key);
        let total = city === finish ? 1 : 0;
        for (let nxt = 0; nxt < locations.length; nxt++) {
            const cost = Math.abs(locations[city] - locations[nxt]);
            if (nxt !== city && cost <= left) total = (total + dp(nxt, left - cost)) % MOD;
        }
        memo.set(key, total);
        return total;
    };
    return dp(start, fuel);
};
