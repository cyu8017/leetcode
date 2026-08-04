// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    const sorted = [...new Set(arr)].sort((a, b) => a - b);
    const rank = new Map(sorted.map((value, i) => [value, i + 1]));
    return arr.map((value) => rank.get(value));
};
