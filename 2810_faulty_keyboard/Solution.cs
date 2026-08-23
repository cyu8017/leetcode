// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

using System;
using System.Text;

public class Solution {
    public string FinalString(string s) {
        var b = new StringBuilder();
        foreach (char c in s) {
            if (c == 'i') {
                char[] arr = b.ToString().ToCharArray();
                Array.Reverse(arr);
                b.Clear();
                b.Append(arr);
            } else b.Append(c);
        }
        return b.ToString();
    }
}
