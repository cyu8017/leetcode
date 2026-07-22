// LeetCode 1624 - Largest Substring Between Two Equal Characters
// https://leetcode.com/problems/largest-substring-between-two-equal-characters/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxLengthBetweenEqualCharacters(string s) {
        var first = new Dictionary<char, int>();
        int ans = -1;
        for (int i = 0; i < s.Length; i++) {
            if (first.TryGetValue(s[i], out int j)) ans = Math.Max(ans, i - j - 1);
            else first[s[i]] = i;
        }
        return ans;
    }
}
