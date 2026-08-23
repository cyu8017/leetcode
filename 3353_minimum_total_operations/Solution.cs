// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(IList<int> nums) {
        int ops = 0;
        for (int i = nums.Count - 2; i >= 0; i--) {
            if (nums[i] != nums[i + 1]) ops++;
        }
        return ops;
    }
}
