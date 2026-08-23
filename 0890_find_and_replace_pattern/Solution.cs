// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> FindAndReplacePattern(string[] words, string pattern) {
        List<int> Normalize(string s) {
            var mapping = new Dictionary<char, int>();
            var outList = new List<int>();
            foreach (char ch in s) {
                if (!mapping.ContainsKey(ch)) mapping[ch] = mapping.Count;
                outList.Add(mapping[ch]);
            }
            return outList;
        }
        var target = Normalize(pattern);
        var ans = new List<string>();
        foreach (var w in words) {
            if (Normalize(w).SequenceEqual(target)) ans.Add(w);
        }
        return ans;
    }
}
