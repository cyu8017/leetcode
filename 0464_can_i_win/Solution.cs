// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

public class Solution {
    private readonly Dictionary<int, bool> memo = new();

    public bool CanIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) {
            return true;
        }
        int total = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (total < desiredTotal) {
            return false;
        }
        return CanWin(0, 0, maxChoosableInteger, desiredTotal);
    }

    private bool CanWin(int state, int currentTotal, int maxChoosableInteger, int desiredTotal) {
        if (memo.TryGetValue(state, out bool cached)) {
            return cached;
        }
        for (int pick = 1; pick <= maxChoosableInteger; pick++) {
            int bit = 1 << (pick - 1);
            if ((state & bit) != 0) {
                continue;
            }
            if (currentTotal + pick >= desiredTotal) {
                memo[state] = true;
                return true;
            }
            if (!CanWin(state | bit, currentTotal + pick, maxChoosableInteger, desiredTotal)) {
                memo[state] = true;
                return true;
            }
        }
        memo[state] = false;
        return false;
    }
}
