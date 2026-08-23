// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

public class Solution {
    public long NumberOfWays(string s) {
        int total0 = 0, total1 = 0;
        foreach (char c in s) {
            if (c == '0') total0++;
            else total1++;
        }
        int left0 = 0, left1 = 0;
        long ans = 0;
        foreach (char c in s) {
            if (c == '0') {
                ans += (long)left1 * (total1 - left1);
                left0++;
            } else {
                ans += (long)left0 * (total0 - left0);
                left1++;
            }
        }
        return ans;
    }
}
