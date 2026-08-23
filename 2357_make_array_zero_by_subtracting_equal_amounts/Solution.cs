// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

using System.Collections.Generic;

public class Solution {
    public int MinimumOperations(int[] nums) {
        var seen = new HashSet<int>();
        foreach (int x in nums) if (x > 0) seen.Add(x);
        return seen.Count;
    }
}
