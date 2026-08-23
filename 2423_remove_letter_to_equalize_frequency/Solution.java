// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean equalFrequency(String word) {
        for (int skip = 0; skip < word.length(); skip++) {
            int[] cnt = new int[26];
            for (int i = 0; i < word.length(); i++) {
                if (i == skip) continue;
                cnt[word.charAt(i) - 'a']++;
            }
            Map<Integer, Integer> freq = new HashMap<>();
            for (int c : cnt) {
                if (c > 0) freq.put(c, freq.getOrDefault(c, 0) + 1);
            }
            if (freq.size() == 1) return true;
        }
        return false;
    }
}
