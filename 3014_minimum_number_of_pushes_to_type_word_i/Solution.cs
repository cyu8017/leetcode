// LeetCode 3014 - Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

public class Solution {
    public int MinimumPushes(string word) {
        int n = word.Length, ans = 0, k = 1;
        for (int i = 0; i < n / 8; i++) {
            ans += k * 8;
            k++;
        }
        ans += k * (n % 8);
        return ans;
    }
}
