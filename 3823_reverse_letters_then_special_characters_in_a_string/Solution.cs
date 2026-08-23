// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReverseByType(string s) {
        var a = new List<char>();
        var b = new List<char>();
        foreach (char c in s) {
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')) a.Add(c);
            else b.Add(c);
        }
        int j = a.Count, k = b.Count;
        var arr = s.ToCharArray();
        for (int i = 0; i < arr.Length; i++) {
            if ((arr[i] >= 'A' && arr[i] <= 'Z') || (arr[i] >= 'a' && arr[i] <= 'z')) arr[i] = a[--j];
            else arr[i] = b[--k];
        }
        return new string(arr);
    }
}
