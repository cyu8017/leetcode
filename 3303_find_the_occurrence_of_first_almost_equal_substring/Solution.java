// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
    public int minStartingIndex(String s, String pattern) {
        int n = s.length(), m = pattern.length();
        for (int i = 0; i + m <= n; i++) {
            int diff = 0;
            for (int j = 0; j < m; j++) {
                if (s.charAt(i + j) != pattern.charAt(j)) {
                    diff++;
                    if (diff > 1) break;
                }
            }
            if (diff <= 1) return i;
        }
        return -1;
    }
}
