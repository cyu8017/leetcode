// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

using System.Collections.Generic;

public class Solution {
    public string[] Spellchecker(string[] wordlist, string[] queries) {
        string Lower(string w) => w.ToLowerInvariant();
        string Devowel(string w) {
            var chars = Lower(w).ToCharArray();
            for (int i = 0; i < chars.Length; i++) {
                char c = chars[i];
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') chars[i] = '*';
            }
            return new string(chars);
        }
        var exact = new HashSet<string>(wordlist);
        var lowerMap = new Dictionary<string, string>();
        var vowelMap = new Dictionary<string, string>();
        foreach (var w in wordlist) {
            string low = Lower(w);
            if (!lowerMap.ContainsKey(low)) lowerMap[low] = w;
            string dv = Devowel(w);
            if (!vowelMap.ContainsKey(dv)) vowelMap[dv] = w;
        }
        var ans = new List<string>();
        foreach (var q in queries) {
            if (exact.Contains(q)) ans.Add(q);
            else if (lowerMap.ContainsKey(Lower(q))) ans.Add(lowerMap[Lower(q)]);
            else if (vowelMap.ContainsKey(Devowel(q))) ans.Add(vowelMap[Devowel(q)]);
            else ans.Add("");
        }
        return ans.ToArray();
    }
}
