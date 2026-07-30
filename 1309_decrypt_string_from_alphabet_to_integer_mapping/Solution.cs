// LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

using System.Text;

public class Solution {
    public string FreqAlphabets(string s) {
        var answer = new StringBuilder();
        int i = s.Length - 1;
        while (i >= 0) {
            if (s[i] == '#') {
                answer.Append((char)(96 + int.Parse(s.Substring(i - 2, 2))));
                i -= 3;
            } else {
                answer.Append((char)(96 + (s[i] - '0')));
                i--;
            }
        }
        var chars = answer.ToString().ToCharArray();
        System.Array.Reverse(chars);
        return new string(chars);
    }
}
