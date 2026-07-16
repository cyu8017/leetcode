// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

public class Solution {
    public IList<int> FindSubstring(string s, string[] words) {
        var result = new List<int>();
        if (words.Length == 0 || s.Length == 0) {
            return result;
        }

        int wordLen = words[0].Length;
        int wordCount = words.Length;
        var need = new Dictionary<string, int>();
        foreach (var word in words) {
            need.TryGetValue(word, out int count);
            need[word] = count + 1;
        }

        for (int start = 0; start < wordLen; start++) {
            int left = start;
            var counts = new Dictionary<string, int>();
            int used = 0;

            for (int right = start; right <= s.Length - wordLen; right += wordLen) {
                string word = s.Substring(right, wordLen);
                if (!need.ContainsKey(word)) {
                    counts.Clear();
                    used = 0;
                    left = right + wordLen;
                    continue;
                }

                counts.TryGetValue(word, out int count);
                counts[word] = count + 1;
                used++;

                while (counts[word] > need[word]) {
                    string leftWord = s.Substring(left, wordLen);
                    counts[leftWord]--;
                    used--;
                    left += wordLen;
                }

                if (used == wordCount) {
                    result.Add(left);
                }
            }
        }

        result.Sort();
        return result;
    }
}
