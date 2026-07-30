// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

using System.Collections.Generic;

public class Solution {
    public int NumSplits(string s) {
        var right = new Dictionary<char, int>();
        foreach (char ch in s) {
            right.TryGetValue(ch, out int c);
            right[ch] = c + 1;
        }
        var left = new HashSet<char>();
        int answer = 0;
        for (int i = 0; i < s.Length - 1; i++) {
            char ch = s[i];
            left.Add(ch);
            right[ch]--;
            if (right[ch] == 0) right.Remove(ch);
            if (left.Count == right.Count) answer++;
        }
        return answer;
    }
}
