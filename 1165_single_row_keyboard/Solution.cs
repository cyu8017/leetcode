// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

using System;
using System.Collections.Generic;

public class Solution {
    public int CalculateTime(string keyboard, string word) {
        var pos = new Dictionary<char, int>();
        for (int i = 0; i < keyboard.Length; i++) pos[keyboard[i]] = i;
        int ans = 0, prev = 0;
        foreach (char ch in word) {
            ans += Math.Abs(pos[ch] - prev);
            prev = pos[ch];
        }
        return ans;
    }
}
