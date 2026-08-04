// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

/**
 * @param {number} num
 * @return {string}
 */
var encode = function(num) {
    return (num + 1).toString(2).slice(1);
};
