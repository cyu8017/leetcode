// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        var stk = new List<int>();
        int ans = 0;
        foreach (int x in nums) {
            while (stk.Count > 0 && stk[stk.Count - 1] > x) {
                ans++;
                stk.RemoveAt(stk.Count - 1);
            }
            if (x != 0 && (stk.Count == 0 || stk[stk.Count - 1] != x)) stk.Add(x);
        }
        ans += stk.Count;
        return ans;
    }
}
