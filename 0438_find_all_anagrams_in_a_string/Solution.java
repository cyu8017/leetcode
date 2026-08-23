// LeetCode 0438 - Find All Anagrams in a String
// https://leetcode.com/problems/find-all-anagrams-in-a-string/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if (p.length() > s.length()) {
            return new ArrayList<>();
        }

        int[] need = new int[26];
        int[] window = new int[26];
        for (int i = 0; i < p.length(); i++) {
            need[p.charAt(i) - 'a']++;
        }

        List<Integer> result = new ArrayList<>();
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            window[s.charAt(right) - 'a']++;
            if (right - left + 1 > p.length()) {
                window[s.charAt(left) - 'a']--;
                left++;
            }
            if (Arrays.equals(window, need)) {
                result.add(left);
            }
        }
        return result;
    }
}
