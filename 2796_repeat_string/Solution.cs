// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/
// JS-only problem; C# stand-in.

using System.Text;

public class Solution {
    public string Replicate(string str, int times) {
        if (times <= 0) return "";
        var sb = new StringBuilder(str.Length * times);
        for (int i = 0; i < times; i++) sb.Append(str);
        return sb.ToString();
    }
}
