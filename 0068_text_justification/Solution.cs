// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> FullJustify(string[] words, int maxWidth) {
        var result = new List<string>();
        int i = 0;

        while (i < words.Length) {
            var lineWords = new List<string>();
            int lineLen = 0;

            while (i < words.Length) {
                string word = words[i];
                int extra = lineWords.Count == 0 ? 0 : 1;
                if (lineLen + word.Length + extra > maxWidth) {
                    break;
                }
                lineWords.Add(word);
                lineLen += word.Length + extra;
                i++;
            }

            if (i == words.Length || lineWords.Count == 1) {
                var line = new StringBuilder();
                for (int j = 0; j < lineWords.Count; j++) {
                    if (j > 0) {
                        line.Append(' ');
                    }
                    line.Append(lineWords[j]);
                }
                line.Append(' ', maxWidth - line.Length);
                result.Add(line.ToString());
            } else {
                int totalChars = 0;
                foreach (string word in lineWords) {
                    totalChars += word.Length;
                }
                int totalSpaces = maxWidth - totalChars;
                int gaps = lineWords.Count - 1;
                int space = totalSpaces / gaps;
                int remainder = totalSpaces % gaps;
                var line = new StringBuilder();
                for (int j = 0; j < lineWords.Count - 1; j++) {
                    line.Append(lineWords[j]);
                    line.Append(' ', space + (j < remainder ? 1 : 0));
                }
                line.Append(lineWords[lineWords.Count - 1]);
                result.Add(line.ToString());
            }
        }

        return result;
    }
}
