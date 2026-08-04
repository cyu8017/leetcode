// LeetCode 1908 - Game of Nim
// https://leetcode.com/problems/game-of-nim/

/**
 * @param {number[]} piles
 * @return {boolean}
 */
var nimGame = function(piles) {
    let x = 0;
    for (const p of piles) x ^= p;
    return x !== 0;
};
