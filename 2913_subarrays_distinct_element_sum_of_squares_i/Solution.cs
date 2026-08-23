// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

using System.Collections.Generic;

public class Solution {
    public int SumCounts(IList<int> nums) {
        int n = nums.Count, ans = 0;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<int>();
            for (int j = i; j < n; j++) {
                seen.Add(nums[j]);
                int d = seen.Count;
                ans += d * d;
            }
        }
        return ans;
    }
}
