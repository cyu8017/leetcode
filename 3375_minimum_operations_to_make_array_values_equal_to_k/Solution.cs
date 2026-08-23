// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums, int k) {
        var seen = new HashSet<int>();
        foreach (int x in nums) {
            if (x < k) return -1;
            if (x > k) seen.Add(x);
        }
        return seen.Count;
    }
}
