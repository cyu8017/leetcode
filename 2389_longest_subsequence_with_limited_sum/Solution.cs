// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

using System;

public class Solution {
    public int[] AnswerQueries(int[] nums, int[] queries) {
        Array.Sort(nums);
        for (int i = 1; i < nums.Length; i++) nums[i] += nums[i - 1];
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int lo = 0, hi = nums.Length;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (nums[mid] <= queries[i]) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = lo;
        }
        return ans;
    }
}
