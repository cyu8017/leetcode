// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

using System;

public class Solution {
    public long PerfectPairs(int[] nums) {
        int n = nums.Length;
        int[] absNums = new int[n];
        for (int i = 0; i < n; i++) absNums[i] = Math.Abs(nums[i]);
        Array.Sort(absNums);
        long ans = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i + 1) j = i + 1;
            while (j < n && absNums[j] <= 2 * absNums[i]) j++;
            ans += j - i - 1;
        }
        return ans;
    }
}
