// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

/**
 * @param {number} n
 * @param {number[]} rounds
 * @return {number[]}
 */
var mostVisited = function(n, rounds) {
    const start = rounds[0], end = rounds[rounds.length - 1];
    if (start <= end) {
        const ans = [];
        for (let i = start; i <= end; i++) ans.push(i);
        return ans;
    }
    const ans = [];
    for (let i = 1; i <= end; i++) ans.push(i);
    for (let i = start; i <= n; i++) ans.push(i);
    return ans;
};
