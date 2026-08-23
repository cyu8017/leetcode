// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

public class Solution {
    public int MinFlips(string target) {
        int ans = 0;
        char prev = '0';
        foreach (char ch in target) {
            if (ch != prev) {
                ans++;
                prev = ch;
            }
        }
        return ans;
    }
}
