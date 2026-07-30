// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] NumSmallerByFrequency(string[] queries, string[] words) {
        int F(string s) {
            char min = s[0];
            foreach (char ch in s) {
                if (ch < min) min = ch;
            }
            int count = 0;
            foreach (char ch in s) {
                if (ch == min) count++;
            }
            return count;
        }

        var freqs = new List<int>();
        foreach (var w in words) freqs.Add(F(w));
        freqs.Sort();

        var ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int target = F(queries[i]);
            int lo = 0, hi = freqs.Count;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (freqs[mid] <= target) lo = mid + 1;
                else hi = mid;
            }
            ans[i] = freqs.Count - lo;
        }
        return ans;
    }
}
