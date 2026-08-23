// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<Integer, Boolean> memo = new HashMap<>();

    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        if (desiredTotal <= 0) {
            return true;
        }
        int total = maxChoosableInteger * (maxChoosableInteger + 1) / 2;
        if (total < desiredTotal) {
            return false;
        }
        return canWin(0, 0, maxChoosableInteger, desiredTotal);
    }

    private boolean canWin(int state, int currentTotal, int maxChoosableInteger, int desiredTotal) {
        Boolean cached = memo.get(state);
        if (cached != null) {
            return cached;
        }
        for (int pick = 1; pick <= maxChoosableInteger; pick++) {
            int bit = 1 << (pick - 1);
            if ((state & bit) != 0) {
                continue;
            }
            if (currentTotal + pick >= desiredTotal) {
                memo.put(state, true);
                return true;
            }
            if (!canWin(state | bit, currentTotal + pick, maxChoosableInteger, desiredTotal)) {
                memo.put(state, true);
                return true;
            }
        }
        memo.put(state, false);
        return false;
    }
}
