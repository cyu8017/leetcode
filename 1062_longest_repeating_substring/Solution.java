// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestRepeatingSubstring(String s) {
        int n = s.length();
        int lo = 1, hi = n - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (hasDup(s, mid)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    private boolean hasDup(String s, int length) {
        Set<String> seen = new HashSet<>();
        for (int i = 0; i + length <= s.length(); i++) {
            String sub = s.substring(i, i + length);
            if (!seen.add(sub)) {
                return true;
            }
        }
        return false;
    }
}
