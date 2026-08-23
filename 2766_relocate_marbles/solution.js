// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

/**
 * @param {number[]} nums
 * @param {number[]} moveFrom
 * @param {number[]} moveTo
 * @return {number[]}
 */
var relocateMarbles = function(nums, moveFrom, moveTo) {
    const pos = new Set(nums);
    for (let i = 0; i < moveFrom.length; i++) {
        pos.delete(moveFrom[i]);
        pos.add(moveTo[i]);
    }
    return [...pos].sort((a, b) => a - b);
};
