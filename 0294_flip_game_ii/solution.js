// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

/**
 * @param {string} currentState
 * @return {boolean}
 */
var canWin = function(currentState) {
    const memo = new Map();

    function canWinState(state) {
        if (memo.has(state)) {
            return memo.get(state);
        }
        for (let index = 0; index < state.length - 1; index += 1) {
            if (state.slice(index, index + 2) === "++") {
                const nextState = `${state.slice(0, index)}--${state.slice(index + 2)}`;
                if (!canWinState(nextState)) {
                    memo.set(state, true);
                    return true;
                }
            }
        }
        memo.set(state, false);
        return false;
    }

    return canWinState(currentState);
};
