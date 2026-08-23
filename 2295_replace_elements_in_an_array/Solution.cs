// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int[] ArrayChange(int[] nums, int[][] operations) {
        var pos = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) pos[nums[i]] = i;
        foreach (var op in operations) {
            int i = pos[op[0]];
            nums[i] = op[1];
            pos.Remove(op[0]);
            pos[op[1]] = i;
        }
        return nums;
    }
}
