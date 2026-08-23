// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

using System.Collections.Generic;
using System.Linq;

public class AutocompleteSystem {
    private readonly Dictionary<string, int> counts = new();
    private string current = "";

    public AutocompleteSystem(string[] sentences, int[] times) {
        for (int i = 0; i < sentences.Length; ++i) {
            counts.TryGetValue(sentences[i], out int c);
            counts[sentences[i]] = c + times[i];
        }
    }

    public IList<string> Input(char c) {
        if (c == '#') {
            counts.TryGetValue(current, out int c0);
            counts[current] = c0 + 1;
            current = "";
            return new List<string>();
        }
        current += c;
        var matches = counts.Keys.Where(s => s.StartsWith(current)).ToList();
        matches.Sort((a, b) => {
            int cmp = counts[b].CompareTo(counts[a]);
            return cmp != 0 ? cmp : string.CompareOrdinal(a, b);
        });
        if (matches.Count > 3) matches = matches.GetRange(0, 3);
        return matches;
    }
}
