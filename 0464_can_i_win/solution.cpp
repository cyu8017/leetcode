// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

#include <unordered_map>

class Solution {
    bool canWinState(int state, int currentTotal, int maxChoosableInteger, int desiredTotal,
                     std::unordered_map<int, bool>& memo) {
        if (memo.count(state)) {
            return memo[state];
        }
        for (int pick = 1; pick <= maxChoosableInteger; ++pick) {
            int bit = 1 << (pick - 1);
            if (state & bit) {
                continue;
            }
            if (currentTotal + pick >= desiredTotal) {
                memo[state] = true;
                return true;
            }
            if (!canWinState(state | bit, currentTotal + pick, maxChoosableInteger, desiredTotal, memo)) {
                memo[state] = true;
                return true;
            }
        }
        memo[state] = false;
        return false;
    }

public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) {
            return true;
        }
        long long total = static_cast<long long>(maxChoosableInteger) * (maxChoosableInteger + 1) / 2;
        if (total < desiredTotal) {
            return false;
        }
        std::unordered_map<int, bool> memo;
        return canWinState(0, 0, maxChoosableInteger, desiredTotal, memo);
    }
};
