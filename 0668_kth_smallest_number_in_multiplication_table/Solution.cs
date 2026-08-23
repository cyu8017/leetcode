// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

public class Solution {
    public int FindKthNumber(int m, int n, int k) {
        int lo = 1, hi = m * n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (CountLe(m, n, mid) >= k) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private int CountLe(int m, int n, int x) {
        int count = 0;
        for (int row = 1; row <= m; ++row) {
            count += System.Math.Min(x / row, n);
        }
        return count;
    }
}
