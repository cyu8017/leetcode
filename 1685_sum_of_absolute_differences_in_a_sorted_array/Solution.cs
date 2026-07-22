// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

using System.Linq;

public class Solution {
    public int[] GetSumAbsoluteDifferences(int[] nums) {
        int total = nums.Sum();
        int left = 0, n = nums.Length;
        var ans = new int[n];
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            ans[i] = x * i - left + (total - left - x) - x * (n - i - 1);
            left += x;
        }
        return ans;
    }
}
