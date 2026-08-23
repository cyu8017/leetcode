// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

public class Solution {
    public IList<string> FindAllConcatenatedWordsInADict(string[] words) {
        Array.Sort(words, (left, right) => left.Length.CompareTo(right.Length));
        HashSet<string> wordSet = new(words);
        List<string> result = new();

        foreach (string word in words) {
            wordSet.Remove(word);
            if (CanForm(word, wordSet)) {
                result.Add(word);
            }
            wordSet.Add(word);
        }
        return result;
    }

    private static bool CanForm(string word, HashSet<string> dictionary) {
        if (word.Length == 0) {
            return true;
        }
        int length = word.Length;
        bool[] dp = new bool[length + 1];
        dp[0] = true;
        for (int end = 1; end <= length; end++) {
            for (int start = 0; start < end; start++) {
                if (dp[start] && dictionary.Contains(word[start..end])) {
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[length];
    }
}
