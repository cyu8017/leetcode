// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

using System.Text;

public class Solution {
    public int MinLength(string s) {
        var st = new StringBuilder();
        foreach (char c in s) {
            if (st.Length > 0 && ((st[st.Length - 1] == 'A' && c == 'B') || (st[st.Length - 1] == 'C' && c == 'D')))
                st.Length--;
            else st.Append(c);
        }
        return st.Length;
    }
}
