// LeetCode 3458 - Select K Disjoint Special Substrings
// https://leetcode.com/problems/select-k-disjoint-special-substrings/

using System;
using System.Collections.Generic;

public class Solution {
    public bool MaxSubstringLength(string s, int k) {
        int n = s.Length;
        int[] first = new int[26], last = new int[26];
        for (int i = 0; i < 26; i++) { first[i] = n; last[i] = -1; }
        for (int i = 0; i < n; i++) {
            int ci = s[i] - 'a';
            if (first[ci] == n) first[ci] = i;
            last[ci] = i;
        }
        var segs = new List<(int l, int r)>();
        for (int c = 0; c < 26; c++) {
            if (last[c] == -1) continue;
            int l = first[c], r = last[c];
            for (int i = l; i <= r; i++) {
                int ci = s[i] - 'a';
                if (first[ci] < l) {
                    l = first[ci];
                    i = l - 1;
                    continue;
                }
                if (last[ci] > r) r = last[ci];
            }
            if (!(l == 0 && r == n - 1)) segs.Add((l, r));
        }
        var uniq = new HashSet<(int, int)>();
        var arr = new List<(int l, int r)>();
        foreach (var sg in segs) {
            if (uniq.Add(sg)) arr.Add(sg);
        }
        arr.Sort((a, b) => a.r.CompareTo(b.r));
        int cnt = 0, end = -1;
        foreach (var sg in arr) {
            if (sg.l > end) {
                cnt++;
                end = sg.r;
            }
        }
        return cnt >= k;
    }
}
