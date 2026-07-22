// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool CanDistribute(int[] nums, int[] quantity) {
        var cnt = nums.GroupBy(x => x).Select(g => g.Count()).ToList();
        Array.Sort(quantity);
        Array.Reverse(quantity);
        int m = quantity.Length;
        int[] sums = new int[1 << m];
        for (int mask = 1; mask < (1 << m); mask++) {
            int bit = mask & -mask;
            sums[mask] = sums[mask ^ bit] + quantity[System.Numerics.BitOperations.TrailingZeroCount(bit)];
        }
        var dp = new HashSet<int> { 0 };
        foreach (int c in cnt) {
            var nxt = new HashSet<int>(dp);
            foreach (int mask in dp) {
                int left = ((1 << m) - 1) ^ mask;
                for (int sub = left; sub > 0; sub = (sub - 1) & left) {
                    if (sums[sub] <= c) nxt.Add(mask | sub);
                }
            }
            dp = nxt;
        }
        return dp.Contains((1 << m) - 1);
    }
}
