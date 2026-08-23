// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

using System.Collections.Generic;

public class Solution {
    public int[] DelayedCount(int[] nums, int k) {
        int n = nums.Length;
        var cnt = new Dictionary<int, int>();
        var ans = new int[n];
        for (int i = n - k - 2; i >= 0; i--) {
            int key = nums[i + k + 1];
            if (!cnt.ContainsKey(key)) cnt[key] = 0;
            cnt[key]++;
            ans[i] = cnt.ContainsKey(nums[i]) ? cnt[nums[i]] : 0;
        }
        return ans;
    }
}
