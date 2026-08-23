// LeetCode 1508 - Range Sum of Sorted Subarray Sums
// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int rangeSum(int[] nums, int n, int left, int right) {
        List<Integer> values = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int total = 0;
            for (int j = i; j < n; j++) {
                total += nums[j];
                values.add(total);
            }
        }
        Collections.sort(values);
        long sum = 0;
        for (int i = left - 1; i < right; i++) {
            sum += values.get(i);
        }
        return (int) (sum % MOD);
    }
}
