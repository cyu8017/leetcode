// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

using System.Text;

public class Solution {
    public string MakeFancyString(string s) {
        var sb = new StringBuilder();
        foreach (char c in s) {
            if (sb.Length >= 2 && sb[sb.Length - 1] == c && sb[sb.Length - 2] == c) continue;
            sb.Append(c);
        }
        return sb.ToString();
    }
}