// LeetCode 0804 - Unique Morse Code Words
// https://leetcode.com/problems/unique-morse-code-words/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int UniqueMorseRepresentations(string[] words) {
        string[] codes = {
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
            "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."
        };
        var seen = new HashSet<string>();
        foreach (string word in words) {
            var sb = new StringBuilder();
            foreach (char ch in word) sb.Append(codes[ch - 'a']);
            seen.Add(sb.ToString());
        }
        return seen.Count;
    }
}
