// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int[] CountWordOccurrences(string[] chunks, string[] queries) {
        var sb = new StringBuilder();
        foreach (string c in chunks) sb.Append(c);
        string s = sb.ToString();
        int n = s.Length;
        var cnt = new Dictionary<string, int>();
        int i = 0;
        while (i < n) {
            if (s[i] == ' ' || s[i] == '-') {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s[j] != ' ' && (s[j] != '-' || (j + 1 < n && s[j + 1] != ' ' && s[j + 1] != '-'))) {
                j++;
            }
            string word = s.Substring(i, j - i);
            if (!cnt.ContainsKey(word)) cnt[word] = 0;
            cnt[word]++;
            i = j;
        }
        int[] ans = new int[queries.Length];
        for (int k = 0; k < queries.Length; k++) {
            ans[k] = cnt.TryGetValue(queries[k], out int v) ? v : 0;
        }
        return ans;
    }
}
