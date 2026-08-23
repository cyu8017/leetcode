// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

class Solution {
    public boolean scoreBalance(String s) {
        int l = 0, r = 0;
        for (char c : s.toCharArray()) r += (c - 'a') + 1;
        for (int i = 0; i + 1 < s.length(); i++) {
            int x = (s.charAt(i) - 'a') + 1;
            l += x;
            r -= x;
            if (l == r) return true;
        }
        return false;
    }
}
