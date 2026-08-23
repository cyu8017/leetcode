// LeetCode 0294 - Flip Game II
// https://leetcode.com/problems/flip-game-ii/

#include <string>
#include <unordered_map>

class Solution {
    bool canWinState(const std::string& state, std::unordered_map<std::string, bool>& memo) {
        if (memo.count(state)) {
            return memo[state];
        }

        for (int index = 0; index + 1 < static_cast<int>(state.size()); index++) {
            if (state[index] == '+' && state[index + 1] == '+') {
                std::string nextState = state;
                nextState[index] = '-';
                nextState[index + 1] = '-';
                if (!canWinState(nextState, memo)) {
                    memo[state] = true;
                    return true;
                }
            }
        }

        memo[state] = false;
        return false;
    }

public:
    bool canWin(std::string currentState) {
        std::unordered_map<std::string, bool> memo;
        return canWinState(currentState, memo);
    }
};
