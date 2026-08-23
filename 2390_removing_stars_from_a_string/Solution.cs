// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

using System.Text;

public class Solution {
    public string RemoveStars(string s) {
        var stack = new StringBuilder();
        foreach (char c in s) {
            if (c == '*') stack.Length--;
            else stack.Append(c);
        }
        return stack.ToString();
    }
}
