// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

using System.Collections.Generic;

public class Solution {
    public long NumberOfSubarrays(int[] nums) {
        var stk = new List<(int, int)>();
        long ans = 0;
        foreach (int x in nums) {
            while (stk.Count > 0 && stk[stk.Count - 1].Item1 < x) stk.RemoveAt(stk.Count - 1);
            if (stk.Count == 0 || stk[stk.Count - 1].Item1 > x) stk.Add((x, 1));
            else {
                var last = stk[stk.Count - 1];
                stk[stk.Count - 1] = (last.Item1, last.Item2 + 1);
            }
            ans += stk[stk.Count - 1].Item2;
        }
        return ans;
    }
}
