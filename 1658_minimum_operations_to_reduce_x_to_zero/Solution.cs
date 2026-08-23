// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

using System;
using System.Linq;

public class Solution {
    public int MinOperations(int[] nums, int x) {
        int target = nums.Sum() - x;
        if (target < 0) return -1;
        int best = -1, left = 0, cur = 0;
        for (int right = 0; right < nums.Length; right++) {
            cur += nums[right];
            while (cur > target) cur -= nums[left++];
            if (cur == target) best = Math.Max(best, right - left + 1);
        }
        return best < 0 ? -1 : nums.Length - best;
    }
}
