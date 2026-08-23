// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var xorGame = function(nums) {
    let x = 0;
    for (const num of nums) x ^= num;
    return x === 0 || nums.length % 2 === 0;
};
