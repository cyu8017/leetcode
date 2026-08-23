// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

using System.Collections.Generic;

public class Solution {
    public long[] MergeAdjacent(int[] nums) {
        var stk = new List<long>();
        foreach (int x in nums) {
            stk.Add(x);
            while (stk.Count > 1 && stk[stk.Count - 1] == stk[stk.Count - 2]) {
                long a = stk[stk.Count - 1];
                stk.RemoveAt(stk.Count - 1);
                long b = stk[stk.Count - 1];
                stk.RemoveAt(stk.Count - 1);
                stk.Add(a + b);
            }
        }
        return stk.ToArray();
    }
}
