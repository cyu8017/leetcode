// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

using System;
using System.Collections.Generic;

public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        Array.Sort(nums);
        var ans = new List<int[]>();
        for (int i = 0; i < nums.Length; i += 3) {
            if (nums[i + 2] - nums[i] > k) return Array.Empty<int[]>();
            ans.Add(new int[] { nums[i], nums[i + 1], nums[i + 2] });
        }
        return ans.ToArray();
    }
}
