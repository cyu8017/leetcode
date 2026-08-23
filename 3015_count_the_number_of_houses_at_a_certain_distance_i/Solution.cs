// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

using System;

public class Solution {
    public int[] CountOfPairs(int n, int x, int y) {
        int[] ans = new int[n];
        x--; y--;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = j - i;
                int b = Math.Abs(x - i) + Math.Abs(y - j) + 1;
                int c = Math.Abs(x - j) + Math.Abs(y - i) + 1;
                ans[Math.Min(a, Math.Min(b, c)) - 1] += 2;
            }
        }
        return ans;
    }
}
