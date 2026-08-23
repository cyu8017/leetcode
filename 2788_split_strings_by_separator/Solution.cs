// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

using System.Collections.Generic;

public class Solution {
    public IList<string> SplitWordsBySeparator(IList<string> words, char separator) {
        var ans = new List<string>();
        foreach (var w in words) {
            int start = 0;
            for (int i = 0; i <= w.Length; i++) {
                if (i == w.Length || w[i] == separator) {
                    if (i > start) ans.Add(w.Substring(start, i - start));
                    start = i + 1;
                }
            }
        }
        return ans;
    }
}
