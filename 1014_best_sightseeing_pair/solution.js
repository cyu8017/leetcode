// LeetCode 1014 - Best Sightseeing Pair
// https://leetcode.com/problems/best-sightseeing-pair/

/**
 * @param {number[]} values
 * @return {number}
 */
var maxScoreSightseeingPair = function(values) {
    let best = values[0];
    let ans = 0;
    for (let j = 1; j < values.length; j++) {
        ans = Math.max(ans, best + values[j] - j);
        best = Math.max(best, values[j] + j);
    }
    return ans;
};
