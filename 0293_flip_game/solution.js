// LeetCode 0293 - Flip Game
// https://leetcode.com/problems/flip-game/

/**
 * @param {string} currentState
 * @return {string[]}
 */
var generatePossibleNextMoves = function(currentState) {
    const result = [];
    for (let index = 0; index < currentState.length - 1; index += 1) {
        if (currentState.slice(index, index + 2) === "++") {
            result.push(`${currentState.slice(0, index)}--${currentState.slice(index + 2)}`);
        }
    }
    return result;
};
