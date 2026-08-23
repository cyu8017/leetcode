// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

using System.Text;

public class Solution {
    public string ClearDigits(string s) {
        var stk = new StringBuilder();
        foreach (char c in s) {
            if (c >= '0' && c <= '9') stk.Length--;
            else stk.Append(c);
        }
        return stk.ToString();
    }
}
