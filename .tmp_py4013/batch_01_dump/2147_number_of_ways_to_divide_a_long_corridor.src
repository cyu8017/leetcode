// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

/**
 * @param {string} corridor
 * @return {number}
 */
var numberOfWays = function(corridor) {
    const MOD = 1000000007;
    const seats = [];
    for (let i = 0; i < corridor.length; i++)
        if (corridor[i] === 'S') seats.push(i);
    if (seats.length === 0 || seats.length % 2 !== 0) return 0;
    let ans = 1;
    for (let i = 2; i < seats.length; i += 2)
        ans = ans * (seats[i] - seats[i - 1]) % MOD;
    return ans;
};
