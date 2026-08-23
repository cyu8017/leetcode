// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

/**
 * @param {number[][]} ranges
 * @return {number}
 */
var countWays = function(ranges) {
    const MOD = 1000000007;
    ranges.sort((a, b) => a[0] - b[0]);
    let groups = 0, end = -1;
    for (const r of ranges) {
        if (r[0] > end) {
            groups++;
            end = r[1];
        } else if (r[1] > end) {
            end = r[1];
        }
    }
    let ans = 1;
    for (let i = 0; i < groups; ++i) ans = ans * 2 % MOD;
    return ans;
};
