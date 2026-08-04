// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

import java.util.*;

class Solution {
    public int numKLenSubstrNoRepeats(String s, int k) {
        if (k > s.length()) return 0;
        Map<Character, Integer> window = new HashMap<>();
        for (int i = 0; i < k; i++) {
            window.merge(s.charAt(i), 1, Integer::sum);
        }
        int ans = window.size() == k ? 1 : 0;
        for (int i = k; i < s.length(); i++) {
            window.merge(s.charAt(i), 1, Integer::sum);
            char left = s.charAt(i - k);
            if (window.merge(left, -1, Integer::sum) == 0) {
                window.remove(left);
            }
            if (window.size() == k) ans++;
        }
        return ans;
    }
}
