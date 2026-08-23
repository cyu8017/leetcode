// LeetCode 0792 - Number of Matching Subsequences
// https://leetcode.com/problems/number-of-matching-subsequences/

using System.Collections.Generic;

public class Solution {
    public int NumMatchingSubseq(string s, string[] words) {
        var waiting = new List<(int wi, int idx)>[128];
        for (int i = 0; i < 128; i++) waiting[i] = new List<(int, int)>();
        for (int i = 0; i < words.Length; i++) waiting[words[i][0]].Add((i, 0));
        int count = 0;
        foreach (char ch in s) {
            var advance = waiting[ch];
            waiting[ch] = new List<(int, int)>();
            foreach (var (wi, idx0) in advance) {
                int idx = idx0 + 1;
                if (idx == words[wi].Length) count++;
                else waiting[words[wi][idx]].Add((wi, idx));
            }
        }
        return count;
    }
}
