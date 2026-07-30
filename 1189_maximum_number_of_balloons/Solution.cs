// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

using System.Collections.Generic;

public class Solution {
    public int MaxNumberOfBalloons(string text) {
        var count = new Dictionary<char, int>();
        foreach (char ch in text) {
            count[ch] = count.GetValueOrDefault(ch) + 1;
        }
        int Get(char ch) => count.GetValueOrDefault(ch);
        return System.Math.Min(Get('b'),
            System.Math.Min(Get('a'),
            System.Math.Min(Get('l') / 2,
            System.Math.Min(Get('o') / 2, Get('n')))));
    }
}
