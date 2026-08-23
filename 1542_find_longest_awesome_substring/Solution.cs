// LeetCode 1542 - Find Longest Awesome Substring
// https://leetcode.com/problems/find-longest-awesome-substring/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestAwesome(string s) {
        var first = new Dictionary<int, int> { [0] = -1 };
        int mask = 0, answer = 0;
        for (int i = 0; i < s.Length; i++) {
            mask ^= 1 << (s[i] - '0');
            if (first.ContainsKey(mask)) answer = Math.Max(answer, i - first[mask]);
            else first[mask] = i;
            for (int bit = 0; bit < 10; bit++) {
                int candidate = mask ^ (1 << bit);
                if (first.ContainsKey(candidate))
                    answer = Math.Max(answer, i - first[candidate]);
            }
        }
        return answer;
    }
}
