// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean canWin(String currentState) {
        return canWinMemo(currentState, new HashMap<>());
    }

    private boolean canWinMemo(String state, Map<String, Boolean> memo) {
        if (memo.containsKey(state)) {
            return memo.get(state);
        }
        for (int index = 0; index < state.length() - 1; index++) {
            if (state.charAt(index) == '+' && state.charAt(index + 1) == '+') {
                String nextState = state.substring(0, index) + "--" + state.substring(index + 2);
                if (!canWinMemo(nextState, memo)) {
                    memo.put(state, true);
                    return true;
                }
            }
        }
        memo.put(state, false);
        return false;
    }
}
