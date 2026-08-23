// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

using System.Collections.Generic;

public class Solution {
    public int[] GoodIndices(string s) {
        var ans = new List<int>();
        for (int i = 0; i < s.Length; i++) {
            string t = i.ToString();
            int k = t.Length;
            if (i + 1 - k >= 0 && s.Substring(i + 1 - k, k) == t) ans.Add(i);
        }
        return ans.ToArray();
    }
}
