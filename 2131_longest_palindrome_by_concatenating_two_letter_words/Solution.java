// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

import java.util.*;

class Solution {
    public int longestPalindrome(String[] words) {
        Map<String, Integer> freq = new HashMap<>();
        for (String w : words) freq.merge(w, 1, Integer::sum);
        int ans = 0;
        boolean center = false;
        for (Map.Entry<String, Integer> kv : freq.entrySet()) {
            String w = kv.getKey();
            int c = kv.getValue();
            String rev = "" + w.charAt(1) + w.charAt(0);
            if (w.charAt(0) == w.charAt(1)) {
                ans += (c / 2) * 4;
                if (c % 2 != 0) center = true;
            } else if (w.compareTo(rev) < 0) {
                ans += Math.min(c, freq.getOrDefault(rev, 0)) * 4;
            }
        }
        if (center) ans += 2;
        return ans;
    }
}
