// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

using System.Collections.Generic;

public class Solution {
    public long MaximumSubarraySum(int[] nums, int k) {
        var cnt = new Dictionary<int, int>();
        long sum = 0, ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            sum += nums[i];
            if (!cnt.ContainsKey(nums[i])) cnt[nums[i]] = 0;
            cnt[nums[i]]++;
            if (i >= k) {
                int y = nums[i - k];
                sum -= y;
                if (--cnt[y] == 0) cnt.Remove(y);
            }
            if (i >= k - 1 && cnt.Count == k && sum > ans) ans = sum;
        }
        return ans;
    }
}
