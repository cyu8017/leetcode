// LeetCode 2730 - Find the Longest Semi-Repetitive Substring
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
    public int longestSemiRepetitiveSubstring(String s) {
        int ans = 0, left = 0, lastPair = -1;
        for (int right = 0; right < s.length(); right++) {
            if (right > 0 && s.charAt(right) == s.charAt(right - 1)) {
                if (lastPair >= left) left = lastPair + 1;
                lastPair = right - 1;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
