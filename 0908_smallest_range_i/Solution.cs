// LeetCode 0908 - Smallest Range I
// https://leetcode.com/problems/smallest-range-i/

using System;
using System.Linq;

public class Solution {
    public int SmallestRangeI(int[] nums, int k) {
        return Math.Max(0, nums.Max() - nums.Min() - 2 * k);
    }
}
