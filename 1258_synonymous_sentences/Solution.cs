// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> GenerateSentences(IList<IList<string>> synonyms, string text) {
        var parent = new Dictionary<string, string>();
        string Find(string x) {
            if (!parent.ContainsKey(x)) parent[x] = x;
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        foreach (var pair in synonyms) {
            string ra = Find(pair[0]), rb = Find(pair[1]);
            parent[ra] = rb;
        }
        var groups = new Dictionary<string, List<string>>();
        foreach (string word in parent.Keys.ToList()) {
            string root = Find(word);
            if (!groups.ContainsKey(root)) groups[root] = new List<string>();
            groups[root].Add(word);
        }
        foreach (var key in groups.Keys.ToList()) groups[key].Sort();

        var words = text.Split(' ');
        var choices = new List<List<string>>();
        foreach (string w in words) {
            if (parent.ContainsKey(w)) choices.Add(groups[Find(w)]);
            else choices.Add(new List<string> { w });
        }
        var answer = new List<string>();
        Dfs(choices, 0, new List<string>(), answer);
        return answer;
    }

    private static void Dfs(List<List<string>> choices, int idx, List<string> cur, List<string> answer) {
        if (idx == choices.Count) {
            answer.Add(string.Join(" ", cur));
            return;
        }
        foreach (string w in choices[idx]) {
            cur.Add(w);
            Dfs(choices, idx + 1, cur, answer);
            cur.RemoveAt(cur.Count - 1);
        }
    }
}
