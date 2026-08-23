// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

public class Solution {
    public int ConvertTime(string current, string correct) {
        int ToMin(string t) =>
            (t[0] - '0') * 600 + (t[1] - '0') * 60 + (t[3] - '0') * 10 + (t[4] - '0');
        int diff = ToMin(correct) - ToMin(current);
        int ans = 0;
        foreach (int step in new[] { 60, 15, 5, 1 }) {
            ans += diff / step;
            diff %= step;
        }
        return ans;
    }
}
