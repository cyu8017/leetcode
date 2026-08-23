// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ApplySubstitutions(IList<IList<string>> replacements, string text) {
        var mp = new Dictionary<string, string>();
        foreach (var r in replacements) mp[r[0]] = r[1];
        string Resolve(string s) {
            var outSb = new StringBuilder();
            for (int i = 0; i < s.Length;) {
                if (s[i] == '%') {
                    int j = i + 1;
                    while (j < s.Length && s[j] != '%') j++;
                    string key = s.Substring(i + 1, j - i - 1);
                    outSb.Append(Resolve(mp[key]));
                    i = j + 1;
                } else {
                    outSb.Append(s[i]);
                    i++;
                }
            }
            return outSb.ToString();
        }
        return Resolve(text);
    }
}
