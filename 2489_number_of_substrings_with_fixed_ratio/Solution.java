// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long fixedRatio(String s, int num1, int num2) {
        Map<Long, Integer> pref = new HashMap<>();
        pref.put(0L, 1);
        int zeros = 0, ones = 0;
        long ans = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') zeros++;
            else ones++;
            long key = 1L * zeros * num2 - 1L * ones * num1;
            ans += pref.getOrDefault(key, 0);
            pref.put(key, pref.getOrDefault(key, 0) + 1);
        }
        return ans;
    }
}
