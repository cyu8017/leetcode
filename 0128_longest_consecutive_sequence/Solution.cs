// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

using System.Collections.Generic;

public class Solution {
    public int LongestConsecutive(int[] nums) {
        var values = new HashSet<int>(nums);
        int best = 0;
        foreach (int num in values) {
            if (values.Contains(num - 1)) continue;
            int length = 1;
            while (values.Contains(num + length)) length++;
            best = System.Math.Max(best, length);
        }
        return best;
    }
}