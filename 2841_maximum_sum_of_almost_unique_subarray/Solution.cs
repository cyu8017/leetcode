// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSum(IList<int> nums, int m, int k) {
        var freq = new Dictionary<int, int>();
        long sum = 0, ans = 0;
        for (int i = 0; i < nums.Count; i++) {
            if (!freq.ContainsKey(nums[i])) freq[nums[i]] = 0;
            freq[nums[i]]++;
            sum += nums[i];
            if (i >= k) {
                int outV = nums[i - k];
                sum -= outV;
                if (--freq[outV] == 0) freq.Remove(outV);
            }
            if (i >= k - 1 && freq.Count >= m) ans = Math.Max(ans, sum);
        }
        return ans;
    }
}
