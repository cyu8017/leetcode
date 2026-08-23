// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

public class Solution {
    public string AddSpaces(string s, int[] spaces) {
        var b = new System.Text.StringBuilder(s.Length + spaces.Length);
        int j = 0;
        for (int i = 0; i < s.Length; i++) {
            if (j < spaces.Length && spaces[j] == i) { b.Append(' '); j++; }
            b.Append(s[i]);
        }
        return b.ToString();
    }
}
