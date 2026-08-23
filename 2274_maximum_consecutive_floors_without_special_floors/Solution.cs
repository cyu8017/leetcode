// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

using System;

public class Solution {
    public int MaxConsecutive(int bottom, int top, int[] special) {
        Array.Sort(special);
        int ans = special[0] - bottom;
        for (int i = 1; i < special.Length; i++)
            ans = Math.Max(ans, special[i] - special[i - 1] - 1);
        ans = Math.Max(ans, top - special[special.Length - 1]);
        return ans;
    }
}
