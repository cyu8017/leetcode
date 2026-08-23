// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

using System.Collections.Generic;

public class Solution {
    private readonly Dictionary<string, string> parent = new Dictionary<string, string>();

    public bool AreSentencesSimilarTwo(string[] sentence1, string[] sentence2, IList<IList<string>> similarPairs) {
        if (sentence1.Length != sentence2.Length) return false;
        parent.Clear();
        foreach (var pair in similarPairs) Unite(pair[0], pair[1]);
        for (int i = 0; i < sentence1.Length; i++) {
            if (Find(sentence1[i]) != Find(sentence2[i])) return false;
        }
        return true;
    }

    private string Find(string x) {
        if (!parent.ContainsKey(x)) parent[x] = x;
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void Unite(string a, string b) => parent[Find(a)] = Find(b);
}
