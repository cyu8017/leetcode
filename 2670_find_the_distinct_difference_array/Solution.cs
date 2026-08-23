// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

using System.Collections.Generic;

public class Solution {
    public int[] DistinctDifferenceArray(int[] nums) {
        int n = nums.Length;
        int[] suf = new int[n + 1];
        var seen = new HashSet<int>();
        for (int i = n - 1; i >= 0; i--) {
            seen.Add(nums[i]);
            suf[i] = seen.Count;
        }
        seen.Clear();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            seen.Add(nums[i]);
            ans[i] = seen.Count - suf[i + 1];
        }
        return ans;
    }
}
