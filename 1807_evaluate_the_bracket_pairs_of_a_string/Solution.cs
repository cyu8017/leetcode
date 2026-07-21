// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string Evaluate(string s, IList<IList<string>> knowledge) {
        var lookup = new Dictionary<string, string>();
        foreach (var pair in knowledge) lookup[pair[0]] = pair[1];

        var sb = new StringBuilder();
        int i = 0;
        while (i < s.Length) {
            if (s[i] == '(') {
                int j = s.IndexOf(')', i + 1);
                string key = s.Substring(i + 1, j - i - 1);
                sb.Append(lookup.TryGetValue(key, out var value) ? value : "?");
                i = j + 1;
            } else {
                sb.Append(s[i]);
                i++;
            }
        }
        return sb.ToString();
    }
}
