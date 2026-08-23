// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ToGoatLatin(string sentence) {
        var vowels = new HashSet<char> { 'a','e','i','o','u','A','E','I','O','U' };
        var parts = sentence.Split(' ');
        var sb = new StringBuilder();
        for (int i = 0; i < parts.Length; i++) {
            if (i > 0) sb.Append(' ');
            string word = parts[i];
            if (vowels.Contains(word[0])) sb.Append(word).Append("ma");
            else sb.Append(word.Substring(1)).Append(word[0]).Append("ma");
            sb.Append('a', i + 1);
        }
        return sb.ToString();
    }
}
