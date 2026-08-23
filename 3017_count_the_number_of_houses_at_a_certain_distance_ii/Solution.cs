// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

using System;

public class Solution {
    public long[] CountOfPairs(int n, int x, int y) {
        if (x > y) { int t = x; x = y; y = t; }
        long[] A = new long[n];
        for (int i = 1; i <= n; i++) {
            A[0] += 2;
            A[(int)Math.Min(i - 1, Math.Abs(i - y) + x)] -= 1;
            A[(int)Math.Min(n - i, Math.Abs(i - x) + 1 + (n - y))] -= 1;
            A[(int)Math.Min(Math.Abs(i - x), Math.Abs(y - i) + 1)] += 1;
            A[(int)Math.Min(Math.Abs(i - x) + 1, Math.Abs(y - i))] += 1;
            long r = Math.Max(x - i, 0) + Math.Max(i - y, 0);
            A[(int)(r + (y - x) / 2)] -= 1;
            A[(int)(r + (y - x + 1) / 2)] -= 1;
        }
        for (int i = 1; i < n; i++) A[i] += A[i - 1];
        return A;
    }
}
