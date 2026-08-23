// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinSwaps(int[] nums) {
        var pos = new List<int>[2];
        pos[0] = new List<int>();
        pos[1] = new List<int>();
        for (int i = 0; i < nums.Length; i++) pos[nums[i] & 1].Add(i);
        if (Math.Abs(pos[0].Count - pos[1].Count) > 1) return -1;
        int Calc(int k) {
            int res = 0;
            for (int i = 0; i < nums.Length; i += 2) res += Math.Abs(pos[k][i / 2] - i);
            return res;
        }
        if (pos[0].Count > pos[1].Count) return Calc(0);
        if (pos[0].Count < pos[1].Count) return Calc(1);
        return Math.Min(Calc(0), Calc(1));
    }
}
