// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

using System.Collections.Generic;

public class Solution {
    public int[] DiStringMatch(string s) {
        int lo = 0, hi = s.Length;
        var ans = new List<int>();
        foreach (char ch in s) {
            if (ch == 'I') ans.Add(lo++);
            else ans.Add(hi--);
        }
        ans.Add(lo);
        return ans.ToArray();
    }
}
