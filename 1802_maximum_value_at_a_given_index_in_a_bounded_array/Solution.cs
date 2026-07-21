// LeetCode 1802 - Maximum Value at a Given Index in a Bounded Array
// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

public class Solution {
    public int MaxValue(int n, int index, int maxSum) {
        long MinSideSum(long value, long count) {
            if (value > count) return (value - 1 + value - count) * count / 2;
            return value * (value - 1) / 2 + (count - value + 1);
        }

        int lo = 1, hi = maxSum;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            long total = MinSideSum(mid, index) + mid + MinSideSum(mid, n - index - 1);
            if (total <= maxSum) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
}
