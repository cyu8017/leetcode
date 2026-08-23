// LeetCode 2811 - Check if it is Possible to Split Array
// https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

using System.Collections.Generic;

public class Solution {
    public bool CanSplitArray(IList<int> nums, int m) {
        int n = nums.Count;
        if (n <= 2) return true;
        for (int i = 0; i + 1 < n; i++) {
            if (nums[i] + nums[i + 1] >= m) return true;
        }
        return false;
    }
}
