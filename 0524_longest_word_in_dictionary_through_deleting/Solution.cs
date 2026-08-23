// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

public class Solution {
    public string FindLongestWord(string s, IList<string> dictionary) {
        string best = "";
        foreach (string word in dictionary) {
            if (IsSubsequence(word, s)
                    && (word.Length > best.Length
                        || (word.Length == best.Length && string.CompareOrdinal(word, best) < 0))) {
                best = word;
            }
        }
        return best;
    }

    private static bool IsSubsequence(string word, string source) {
        int index = 0;
        for (int pos = 0; pos < source.Length; pos++) {
            if (index < word.Length && word[index] == source[pos]) {
                index++;
            }
        }
        return index == word.Length;
    }
}
