// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

using System.Collections.Generic;

public class Solution {
    public bool FindSubarrays(int[] nums) {
        var seen = new HashSet<int>();
        for (int i = 0; i + 1 < nums.Length; i++) {
            int s = nums[i] + nums[i + 1];
            if (seen.Contains(s)) return true;
            seen.Add(s);
        }
        return false;
    }
}
