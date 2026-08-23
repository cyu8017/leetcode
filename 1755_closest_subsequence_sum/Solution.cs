// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

public class Solution {
    public int MinAbsDifference(int[] nums, int goal) {
        int n = nums.Length;
        int[] left = nums[..(n / 2)];
        int[] right = nums[(n / 2)..];

        long[] a = Sums(left);
        long[] b = Sums(right);
        long best = long.MaxValue;
        int j = b.Length - 1;
        foreach (long x in a) {
            while (j > 0 && Math.Abs(x + b[j] - goal) >= Math.Abs(x + b[j - 1] - goal)) {
                j--;
            }
            best = Math.Min(best, Math.Abs(x + b[j] - goal));
        }
        return (int) best;
    }

    private long[] Sums(int[] arr) {
        long[] vals = new long[1 << arr.Length];
        int size = 1;
        foreach (int x in arr) {
            for (int i = 0; i < size; i++) {
                vals[size + i] = vals[i] + x;
            }
            size *= 2;
        }
        Array.Sort(vals);
        return vals;
    }
}
