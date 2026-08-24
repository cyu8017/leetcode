// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution {
    private long count(String s, char a, char b) {
        long ca = 0, ans = 0;
        for (char c : s.toCharArray()) {
            if (c == b) ans += ca;
            if (c == a) ca++;
        }
        return ans;
    }

    public long maximumSubsequenceCount(String text, String pattern) {
        char a = pattern.charAt(0), b = pattern.charAt(1);
        return Math.max(count(a + text, a, b), count(text + b, a, b));
    }
}
