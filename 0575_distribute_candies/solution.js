// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

/**
 * @param {number[]} candyType
 * @return {number}
 */
var distributeCandies = function(candyType) {
    return Math.min(new Set(candyType).size, Math.floor(candyType.length / 2));
};
