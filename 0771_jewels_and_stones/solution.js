// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    const jewelSet = new Set(jewels);
    let count = 0;
    for (const stone of stones) if (jewelSet.has(stone)) count++;
    return count;
};
