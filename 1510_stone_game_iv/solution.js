// LeetCode 1510 - Stone Game IV
// https://leetcode.com/problems/stone-game-iv/

/**
 * @param {number} n
 * @return {boolean}
 */
var winnerSquareGame = function(n) {
    const win = Array(n + 1).fill(false);
    for (let value = 1; value <= n; value++) {
        for (let root = 1; root * root <= value; root++) {
            if (!win[value - root * root]) {
                win[value] = true;
                break;
            }
        }
    }
    return win[n];
};
