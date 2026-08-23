// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReplaceWords(IList<string> dictionary, string sentence) {
        var roots = new HashSet<string>(dictionary);
        string[] words = sentence.Split(' ');
        var result = new StringBuilder();
        for (int w = 0; w < words.Length; ++w) {
            string word = words[w];
            string replacement = word;
            for (int i = 1; i <= word.Length; ++i) {
                string prefix = word.Substring(0, i);
                if (roots.Contains(prefix)) {
                    replacement = prefix;
                    break;
                }
            }
            if (w > 0) result.Append(' ');
            result.Append(replacement);
        }
        return result.ToString();
    }
}
