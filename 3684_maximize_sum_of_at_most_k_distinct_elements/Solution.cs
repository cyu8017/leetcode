// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] MaxKDistinct(int[] nums, int k) {
        Array.Sort(nums);
        int n = nums.Length;
        var ans = new List<int>();
        for (int i = n - 1; i >= 0; i--) {
            if (i + 1 < n && nums[i] == nums[i + 1]) continue;
            ans.Add(nums[i]);
            if (--k == 0) break;
        }
        return ans.ToArray();
    }
}
