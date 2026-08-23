// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
    public int longestContinuousSubstring(String s) {
        int ans = 1, cur = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1) + 1) {
                cur++;
                ans = Math.max(ans, cur);
            } else {
                cur = 1;
            }
        }
        return ans;
    }
}
