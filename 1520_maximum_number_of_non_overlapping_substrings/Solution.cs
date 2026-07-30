// LeetCode 1520 - Maximum Number of Non-Overlapping Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> MaxNumOfSubstrings(string s) {
        int[] first = new int[26];
        int[] last = new int[26];
        Array.Fill(first, -1);
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        var intervals = new List<(int end, int start)>();
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            if (first[c] != i) continue;
            int end = last[c];
            bool valid = true;
            for (int j = i; j <= end; j++) {
                int cj = s[j] - 'a';
                if (first[cj] < i) { valid = false; break; }
                end = Math.Max(end, last[cj]);
            }
            if (valid) intervals.Add((end, i));
        }
        intervals.Sort();
        var answer = new List<string>();
        int previousEnd = -1;
        foreach (var (end, start) in intervals) {
            if (start > previousEnd) {
                answer.Add(s.Substring(start, end - start + 1));
                previousEnd = end;
            }
        }
        return answer.OrderBy(x => x.Length).ToList();
    }
}
