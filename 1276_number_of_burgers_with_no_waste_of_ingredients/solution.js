// LeetCode 1276 - Number of Burgers with No Waste of Ingredients
// https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

/**
 * @param {number} tomatoSlices
 * @param {number} cheeseSlices
 * @return {number[]}
 */
var numOfBurgers = function(tomatoSlices, cheeseSlices) {
    if (tomatoSlices % 2 !== 0) return [];
    const jumbo = tomatoSlices / 2 - cheeseSlices;
    const small = cheeseSlices - jumbo;
    return jumbo >= 0 && small >= 0 ? [jumbo, small] : [];
};
