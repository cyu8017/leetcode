// LeetCode 1573 - Number of Ways to Split a String
// https://leetcode.com/problems/number-of-ways-to-split-a-string/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numWays(String s) {
        int ones = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ones++;
            }
        }
        if (ones % 3 != 0) {
            return 0;
        }
        if (ones == 0) {
            long gaps = s.length() - 1L;
            return (int) (gaps * (gaps - 1) / 2 % MOD);
        }
        int target = ones / 3;
        List<Integer> positions = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                positions.add(i);
            }
        }
        long result = 1L * (positions.get(target) - positions.get(target - 1))
                * (positions.get(2 * target) - positions.get(2 * target - 1));
        return (int) (result % MOD);
    }
}
