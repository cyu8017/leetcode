// LeetCode 2389 - Longest Subsequence With Limited Sum
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

import java.util.Arrays;

class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) nums[i] += nums[i - 1];
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int lo = 0, hi = nums.length;
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
