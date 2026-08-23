// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MergeCharacters(string s, int k) {
        var last = new Dictionary<char, int>();
        var ans = new StringBuilder();
        foreach (char c in s) {
            int cur = ans.Length;
            if (last.ContainsKey(c) && cur - last[c] <= k) continue;
            ans.Append(c);
            last[c] = cur;
        }
        return ans.ToString();
    }
}
