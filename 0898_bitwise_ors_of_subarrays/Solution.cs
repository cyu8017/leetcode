// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

using System.Collections.Generic;

public class Solution {
    public int SubarrayBitwiseORs(int[] arr) {
        var ans = new HashSet<int>();
        var cur = new HashSet<int>();
        foreach (int x in arr) {
            var nxt = new HashSet<int> { x };
            foreach (int y in cur) nxt.Add(x | y);
            cur = nxt;
            foreach (int v in cur) ans.Add(v);
        }
        return ans.Count;
    }
}
