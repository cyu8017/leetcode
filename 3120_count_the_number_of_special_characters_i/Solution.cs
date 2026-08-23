// LeetCode 3120 - Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/

public class Solution {
    public int NumberOfSpecialChars(string word) {
        bool[] s = new bool[128];
        foreach (char c in word) s[c] = true;
        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (s['a' + i] && s['A' + i]) ans++;
        }
        return ans;
    }
}
