// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

using System.Text;

public class Solution {
    public string AddBoldTag(string s, string[] words) {
        int n = s.Length;
        bool[] bold = new bool[n];
        foreach (string word in words) {
            int start = s.IndexOf(word, System.StringComparison.Ordinal);
            while (start >= 0) {
                for (int i = start; i < start + word.Length; ++i) bold[i] = true;
                start = s.IndexOf(word, start + 1, System.StringComparison.Ordinal);
            }
        }
        var parts = new StringBuilder();
        int i2 = 0;
        while (i2 < n) {
            if (bold[i2]) {
                parts.Append("<b>");
                while (i2 < n && bold[i2]) parts.Append(s[i2++]);
                parts.Append("</b>");
            } else {
                parts.Append(s[i2++]);
            }
        }
        return parts.ToString();
    }
}
