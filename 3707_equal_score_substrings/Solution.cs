// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

public class Solution {
    public bool ScoreBalance(string s) {
        int l = 0, r = 0;
        foreach (char c in s) r += (c - 'a') + 1;
        for (int i = 0; i + 1 < s.Length; i++) {
            int x = (s[i] - 'a') + 1;
            l += x;
            r -= x;
            if (l == r) return true;
        }
        return false;
    }
}
