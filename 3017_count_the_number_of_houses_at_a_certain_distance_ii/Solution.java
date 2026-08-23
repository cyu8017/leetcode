// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

class Solution {
    public long[] countOfPairs(int n, int x, int y) {
        if (x > y) { int t = x; x = y; y = t; }
        long[] A = new long[n];
        for (int i = 1; i <= n; i++) {
            A[0] += 2;
            A[(int)Math.min(i - 1, Math.abs(i - y) + x)] -= 1;
            A[(int)Math.min(n - i, Math.abs(i - x) + 1 + (n - y))] -= 1;
            A[(int)Math.min(Math.abs(i - x), Math.abs(y - i) + 1)] += 1;
            A[(int)Math.min(Math.abs(i - x) + 1, Math.abs(y - i))] += 1;
            long r = Math.max(x - i, 0) + Math.max(i - y, 0);
            A[(int)(r + (y - x) / 2)] -= 1;
            A[(int)(r + (y - x + 1) / 2)] -= 1;
        }
        for (int i = 1; i < n; i++) A[i] += A[i - 1];
        return A;
    }
}
