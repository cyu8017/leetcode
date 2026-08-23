// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

using System.Collections.Generic;

public class MagicDictionary {
    private List<string> words = new();

    public MagicDictionary() {}

    public void BuildDict(string[] dictionary) {
        words = new List<string>(dictionary);
    }

    public bool Search(string searchWord) {
        foreach (string word in words) {
            if (word.Length != searchWord.Length) continue;
            int diff = 0;
            for (int i = 0; i < word.Length; ++i) {
                if (word[i] != searchWord[i]) ++diff;
            }
            if (diff == 1) return true;
        }
        return false;
    }
}
