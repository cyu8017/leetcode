// LeetCode 1823 - Find the Winner of the Circular Game
// https://leetcode.com/problems/find-the-winner-of-the-circular-game/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let pos = 0;
    for (let size = 2; size <= n; size++) {
        pos = (pos + k) % size;
    }
    return pos + 1;
};
