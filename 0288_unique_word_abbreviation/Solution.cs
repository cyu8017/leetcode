// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

using System.Collections.Generic;

public class ValidWordAbbr {
    private readonly Dictionary<string, HashSet<string>> groups = new();

    public ValidWordAbbr(string[] dictionary) {
        foreach (string word in dictionary) {
            string key = Abbreviate(word);
            if (!groups.TryGetValue(key, out HashSet<string>? words)) {
                words = new HashSet<string>();
                groups[key] = words;
            }
            words.Add(word);
        }
    }

    public bool IsUnique(string word) {
        string key = Abbreviate(word);
        if (!groups.TryGetValue(key, out HashSet<string>? words)) {
            return true;
        }
        return words.Count == 0 || (words.Count == 1 && words.Contains(word));
    }

    private static string Abbreviate(string word) {
        if (word.Length <= 2) {
            return word;
        }
        return $"{word[0]}{word.Length - 2}{word[^1]}";
    }
}
