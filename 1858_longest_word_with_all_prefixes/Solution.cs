// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

public class Solution {
    public string LongestWord(string[] words) {
        var wordSet = new HashSet<string>(words);
        string best = "";
        foreach (string word in words) {
            bool valid = true;
            for (int len = word.Length; len > 0; len--) {
                if (!wordSet.Contains(word.Substring(0, len))) {
                    valid = false;
                    break;
                }
            }
            if (valid && (word.Length > best.Length || (word.Length == best.Length && string.CompareOrdinal(word, best) < 0))) {
                best = word;
            }
        }
        return best;
    }
}
