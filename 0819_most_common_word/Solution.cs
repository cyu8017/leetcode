// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MostCommonWord(string paragraph, string[] banned) {
        var bannedSet = new HashSet<string>(banned);
        var counts = new Dictionary<string, int>();
        var word = new StringBuilder();
        string best = "";
        int bestCount = 0;
        void Flush() {
            if (word.Length == 0) return;
            string w = word.ToString();
            word.Clear();
            if (bannedSet.Contains(w)) return;
            if (!counts.ContainsKey(w)) counts[w] = 0;
            int c = ++counts[w];
            if (c > bestCount) { bestCount = c; best = w; }
        }
        foreach (char ch in paragraph) {
            if (char.IsLetter(ch)) word.Append(char.ToLower(ch));
            else Flush();
        }
        Flush();
        return best;
    }
}
