// LeetCode 0120 - Triangle
// https://leetcode.com/problems/triangle/

/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    const dp = [...triangle[triangle.length - 1]];
    for (let rowIndex = triangle.length - 2; rowIndex >= 0; rowIndex--) {
        for (let column = 0; column < triangle[rowIndex].length; column++) {
            dp[column] = triangle[rowIndex][column] + Math.min(dp[column], dp[column + 1]);
        }
    }
    return dp[0];
};