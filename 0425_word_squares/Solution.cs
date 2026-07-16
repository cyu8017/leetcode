// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public IList<IList<string>> WordSquares(string[] words) {
        string[] sortedWords = words.OrderBy(word => word).ToArray();
        int length = sortedWords[0].Length;
        Dictionary<string, List<string>> prefixMap = new() {
            [""] = sortedWords.ToList(),
        };
        foreach (string word in sortedWords) {
            for (int index = 0; index < word.Length; index++) {
                string prefix = word.Substring(0, index + 1);
                if (!prefixMap.ContainsKey(prefix)) {
                    prefixMap[prefix] = new List<string>();
                }
                prefixMap[prefix].Add(word);
            }
        }

        IList<IList<string>> squares = new List<IList<string>>();
        List<string> current = new();

        void Dfs(int row) {
            if (row == length) {
                squares.Add(new List<string>(current));
                return;
            }
            StringBuilder prefixBuilder = new();
            foreach (string word in current) {
                prefixBuilder.Append(word[row]);
            }
            string prefix = prefixBuilder.ToString();
            if (!prefixMap.TryGetValue(prefix, out List<string>? candidates)) {
                return;
            }
            foreach (string candidate in candidates) {
                current.Add(candidate);
                Dfs(row + 1);
                current.RemoveAt(current.Count - 1);
            }
        }

        Dfs(0);
        return squares;
    }
}
