// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

using System.Collections.Generic;

public class WordFilter {
    private readonly Dictionary<string, int> lookup = new Dictionary<string, int>();

    public WordFilter(string[] words) {
        for (int index = 0; index < words.Length; index++) {
            string word = words[index];
            int size = word.Length;
            for (int i = 0; i <= size; i++) {
                for (int j = 0; j <= size; j++) {
                    lookup[word.Substring(0, i) + "#" + word.Substring(j)] = index;
                }
            }
        }
    }

    public int F(string pref, string suff) {
        string key = pref + "#" + suff;
        return lookup.TryGetValue(key, out int index) ? index : -1;
    }
}
