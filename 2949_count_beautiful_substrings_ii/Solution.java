// LeetCode 2949 - Count Beautiful Substrings II
// https://leetcode.com/problems/count-beautiful-substrings-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    public long beautifulSubstrings(String s, int k) {
        int x = 1;
        while ((x * x) % k != 0) x++;
        Map<Long, Integer> freq = new HashMap<>();
        freq.put(0L, 1);
        int bal = 0, vowels = 0;
        long ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (isVowel(ch)) { bal++; vowels++; }
            else bal--;
            long kk = (((long) bal) << 32) | (vowels % x);
            int f = freq.getOrDefault(kk, 0);
            ans += f;
            freq.put(kk, f + 1);
        }
        return ans;
    }
}
