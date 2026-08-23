// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string BetterCompression(string compressed) {
        var cnt = new Dictionary<char, int>();
        int n = compressed.Length;
        for (int i = 0; i < n; ) {
            char c = compressed[i];
            int j = i + 1, x = 0;
            while (j < n && compressed[j] >= '0' && compressed[j] <= '9') {
                x = x * 10 + (compressed[j] - '0');
                j++;
            }
            if (!cnt.ContainsKey(c)) cnt[c] = 0;
            cnt[c] += x;
            i = j;
        }
        var ans = new StringBuilder();
        for (char c = 'a'; c <= 'z'; c++) {
            if (cnt.TryGetValue(c, out int v) && v > 0) {
                ans.Append(c);
                ans.Append(v);
            }
        }
        return ans.ToString();
    }
}
