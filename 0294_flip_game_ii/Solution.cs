// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

using System.Collections.Generic;

public class Solution {
    public bool CanWin(string currentState) {
        return CanWinMemo(currentState, new Dictionary<string, bool>());
    }

    private bool CanWinMemo(string state, Dictionary<string, bool> memo) {
        if (memo.TryGetValue(state, out bool cached)) {
            return cached;
        }
        for (int index = 0; index < state.Length - 1; index++) {
            if (state[index] == '+' && state[index + 1] == '+') {
                string nextState = state.Substring(0, index) + "--" + state.Substring(index + 2);
                if (!CanWinMemo(nextState, memo)) {
                    memo[state] = true;
                    return true;
                }
            }
        }
        memo[state] = false;
        return false;
    }
}
