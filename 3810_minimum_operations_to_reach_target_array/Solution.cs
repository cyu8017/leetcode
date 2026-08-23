// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums, int[] target) {
        var s = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] != target[i]) s.Add(nums[i]);
        }
        return s.Count;
    }
}
