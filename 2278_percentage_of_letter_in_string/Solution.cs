// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

public class Solution {
    public int PercentageLetter(string s, char letter) {
        int cnt = 0;
        foreach (char c in s) if (c == letter) cnt++;
        return cnt * 100 / s.Length;
    }
}
