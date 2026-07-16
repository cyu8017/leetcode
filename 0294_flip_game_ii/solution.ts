// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

export function canWin(currentState: string): boolean {
    const memo = new Map<string, boolean>();

    function canWinState(state: string): boolean {
        if (memo.has(state)) {
            return memo.get(state) as boolean;
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
}
