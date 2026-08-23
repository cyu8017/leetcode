// LeetCode 2781 - Length of the Longest Valid Substring
// https://leetcode.com/problems/length-of-the-longest-valid-substring/

import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int longestValidSubstring(String word, List<String> forbidden) {
        Set<String> forbid = new HashSet<>();
        int maxLen = 0;
        for (String f : forbidden) {
            forbid.add(f);
            maxLen = Math.max(maxLen, f.length());
        }
        int ans = 0, right = word.length() - 1;
        for (int left = word.length() - 1; left >= 0; left--) {
            for (int k = left; k <= right && k - left + 1 <= maxLen; k++) {
                if (forbid.contains(word.substring(left, k + 1))) {
                    right = k - 1;
                    break;
                }
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
