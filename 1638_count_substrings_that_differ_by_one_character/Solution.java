// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution {
    public int countSubstrings(String s, String t) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j < t.length(); j++) {
                int diff = 0;
                for (int k = 0; k < Math.min(s.length() - i, t.length() - j); k++) {
                    if (s.charAt(i + k) != t.charAt(j + k)) diff++;
                    if (diff == 1) ans++;
                    else if (diff > 1) break;
                }
            }
        }
        return ans;
    }
}
