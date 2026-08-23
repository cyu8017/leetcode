// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> PartitionLabels(string s) {
        int[] last = new int[26];
        for (int i = 0; i < s.Length; i++) last[s[i] - 'a'] = i;
        int start = 0, end = 0;
        var answer = new List<int>();
        for (int i = 0; i < s.Length; i++) {
            end = Math.Max(end, last[s[i] - 'a']);
            if (i == end) {
                answer.Add(end - start + 1);
                start = i + 1;
            }
        }
        return answer;
    }
}
