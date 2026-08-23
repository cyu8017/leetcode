// LeetCode 2799 - Count Complete Subarrays in an Array
// https://leetcode.com/problems/count-complete-subarrays-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int CountCompleteSubarrays(int[] nums) {
        int need = new HashSet<int>(nums).Count, ans = 0, n = nums.Length;
        for (int i = 0; i < n; i++) {
            var seen = new HashSet<int>();
            for (int j = i; j < n; j++) {
                seen.Add(nums[j]);
                if (seen.Count == need) {
                    ans += n - j;
                    break;
                }
            }
        }
        return ans;
    }
}
