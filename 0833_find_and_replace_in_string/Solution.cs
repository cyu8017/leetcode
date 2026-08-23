// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string FindReplaceString(string s, int[] indices, string[] sources, string[] targets) {
        var replace = new Dictionary<int, (int len, string target)>();
        for (int k = 0; k < indices.Length; k++) {
            int i = indices[k];
            if (i + sources[k].Length <= s.Length && s.Substring(i, sources[k].Length) == sources[k])
                replace[i] = (sources[k].Length, targets[k]);
        }
        var sb = new StringBuilder();
        int pos = 0, n = s.Length;
        while (pos < n) {
            if (replace.TryGetValue(pos, out var r)) {
                sb.Append(r.target);
                pos += r.len;
            } else {
                sb.Append(s[pos]);
                pos++;
            }
        }
        return sb.ToString();
    }
}
