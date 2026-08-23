// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

import java.util.*;

class Solution {
    public int equalDigitFrequency(String s) {
        int n = s.length();
        Set<String> seen = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int[] freq = new int[10];
            int maxf = 0, kinds = 0;
            for (int j = i; j < n; j++) {
                int d = s.charAt(j) - '0';
                if (freq[d] == 0) kinds++;
                freq[d]++;
                maxf = Math.max(maxf, freq[d]);
                if (maxf * kinds == j - i + 1) seen.add(s.substring(i, j + 1));
            }
        }
        return seen.size();
    }
}
