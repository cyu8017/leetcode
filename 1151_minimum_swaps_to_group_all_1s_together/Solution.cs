// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

using System;
using System.Linq;

public class Solution {
    public int MinSwaps(int[] data) {
        int ones = data.Sum();
        if (ones <= 1) return 0;
        int cur = data.Take(ones).Sum();
        int best = cur;
        for (int i = ones; i < data.Length; i++) {
            cur += data[i] - data[i - ones];
            best = Math.Max(best, cur);
        }
        return ones - best;
    }
}
