// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

using System.Collections.Generic;

public class Solution {
    public int ShortestMatchingSubstring(string s, string p) {
        var parts = new List<string>();
        string cur = "";
        foreach (char c in p) {
            if (c == '*') {
                parts.Add(cur);
                cur = "";
            } else cur += c;
        }
        parts.Add(cur);
        while (parts.Count < 3) parts.Add("");
        string a = parts[0], b = parts[1], c = parts[2];
        int n = s.Length;
        List<int> FindAll(string sub) {
            var res = new List<int>();
            if (sub.Length == 0) {
                for (int i = 0; i <= n; i++) res.Add(i);
                return res;
            }
            for (int i = 0; i + sub.Length <= n; i++) {
                if (string.CompareOrdinal(s, i, sub, 0, sub.Length) == 0) res.Add(i);
            }
            return res;
        }
        int SortSearch(List<int> arr, int x) {
            int lo = 0, hi = arr.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        }
        var posA = FindAll(a);
        var posB = FindAll(b);
        var posC = FindAll(c);
        int ans = n + 1;
        foreach (int ia in posA) {
            int endA = ia + a.Length;
            int bi = SortSearch(posB, endA);
            for (; bi < posB.Count; bi++) {
                int endB = posB[bi] + b.Length;
                int ci = SortSearch(posC, endB);
                if (ci < posC.Count) {
                    int length = posC[ci] + c.Length - ia;
                    if (length < ans) ans = length;
                }
                break;
            }
        }
        return ans == n + 1 ? -1 : ans;
    }
}
