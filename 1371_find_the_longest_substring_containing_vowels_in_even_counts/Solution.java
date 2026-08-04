// LeetCode 1371 - Find The Longest Substring Containing Vowels In Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

import java.util.*;

class Solution {
    public int findTheLongestSubstring(String s) {
        Map<Integer, Integer> first = new HashMap<>();
        first.put(0, -1);
        int mask = 0, ans = 0;
        String vowels = "aeiou";
        for (int i = 0; i < s.length(); i++) {
            int idx = vowels.indexOf(s.charAt(i));
            if (idx >= 0) mask ^= 1 << idx;
            if (first.containsKey(mask)) ans = Math.max(ans, i - first.get(mask));
            else first.put(mask, i);
        }
        return ans;
    }
}
