// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

using System;

public class Solution {
    public long SumDigitDifferences(int[] nums) {
        int n = nums.Length;
        int m = (int)Math.Floor(Math.Log10(nums[0])) + 1;
        long ans = 0;
        for (int k = 0; k < m; k++) {
            int[] cnt = new int[10];
            for (int i = 0; i < n; i++) {
                cnt[nums[i] % 10]++;
                nums[i] /= 10;
            }
            foreach (int v in cnt) ans += 1L * v * (n - v);
        }
        return ans / 2;
    }
}
