// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

public class Solution {
    public string[] WordsAbbreviation(string[] words) {
        int[] prefixes = Enumerable.Repeat(1, words.Length).ToArray();
        bool changed = true;
        while (changed) {
            changed = false;
            Dictionary<string, List<int>> groups = new();
            for (int index = 0; index < words.Length; index++) {
                string key = Abbreviate(words[index], prefixes[index]);
                if (!groups.TryGetValue(key, out List<int>? indices)) {
                    indices = new List<int>();
                    groups[key] = indices;
                }
                indices.Add(index);
            }
            foreach (List<int> indices in groups.Values) {
                if (indices.Count > 1) {
                    changed = true;
                    foreach (int index in indices) {
                        prefixes[index]++;
                    }
                }
            }
        }
        return words.Select((word, index) => Abbreviate(word, prefixes[index])).ToArray();
    }

    private static string Abbreviate(string word, int prefix) {
        if (prefix + 2 >= word.Length) {
            return word;
        }
        int middle = word.Length - prefix - 1;
        string candidate = word[..prefix] + middle + word[^1];
        return candidate.Length < word.Length ? candidate : word;
    }
}
