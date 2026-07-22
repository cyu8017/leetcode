// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string FindLexSmallestString(string s, int a, int b) {
        var seen = new HashSet<string> { s };
        var q = new Queue<string>();
        q.Enqueue(s);
        string ans = s;
        while (q.Count > 0) {
            string cur = q.Dequeue();
            if (string.CompareOrdinal(cur, ans) < 0) ans = cur;
            var sb = new StringBuilder(cur.Length);
            for (int i = 0; i < cur.Length; i++) {
                int d = cur[i] - '0';
                if (i % 2 == 1) d = (d + a) % 10;
                sb.Append((char)('0' + d));
            }
            string add = sb.ToString();
            string rot = cur[^b..] + cur[..^b];
            foreach (string nxt in new[] { add, rot }) {
                if (seen.Add(nxt)) q.Enqueue(nxt);
            }
        }
        return ans;
    }
}
