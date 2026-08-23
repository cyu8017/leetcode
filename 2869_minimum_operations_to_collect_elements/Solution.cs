// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(IList<int> nums, int k) {
        var need = new HashSet<int>();
        for (int i = 1; i <= k; i++) need.Add(i);
        for (int i = nums.Count - 1; i >= 0; i--) {
            need.Remove(nums[i]);
            if (need.Count == 0) return nums.Count - i;
        }
        return nums.Count;
    }
}
