// LeetCode 1755 - Closest Subsequence Sum
// https://leetcode.com/problems/closest-subsequence-sum/

import java.util.Arrays;

class Solution {
    public int minAbsDifference(int[] nums, int goal) {
        int n = nums.length;
        int[] left = Arrays.copyOfRange(nums, 0, n / 2);
        int[] right = Arrays.copyOfRange(nums, n / 2, n);

        long[] a = sums(left);
        long[] b = sums(right);
        long best = Long.MAX_VALUE;
        int j = b.length - 1;
        for (long x : a) {
            while (j > 0 && Math.abs(x + b[j] - goal) >= Math.abs(x + b[j - 1] - goal)) {
                j--;
            }
            best = Math.min(best, Math.abs(x + b[j] - goal));
        }
        return (int) best;
    }

    private long[] sums(int[] arr) {
        long[] vals = new long[1 << arr.length];
        int size = 1;
        for (int x : arr) {
            for (int i = 0; i < size; i++) {
                vals[size + i] = vals[i] + x;
            }
            size *= 2;
        }
        Arrays.sort(vals);
        return vals;
    }
}
