// LeetCode 3846 - Total Distance To Type A String Using One Finger
// https://leetcode.com/problems/total-distance-to-type-a-string-using-one-finger/

using System;
using System.Collections.Generic;

public class Solution {
    static Dictionary<char, (int, int)> BuildPos() {
        var pos = new Dictionary<char, (int, int)>();
        string[] keys = { "qwertyuiop", "asdfghjkl", "zxcvbnm" };
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < keys[i].Length; j++) pos[keys[i][j]] = (i, j);
        }
        return pos;
    }
    static readonly Dictionary<char, (int, int)> Pos = BuildPos();

    public int TotalDistance(string s) {
        char pre = 'a';
        int ans = 0;
        foreach (char cur in s) {
            var p1 = Pos[pre];
            var p2 = Pos[cur];
            ans += Math.Abs(p1.Item1 - p2.Item1) + Math.Abs(p1.Item2 - p2.Item2);
            pre = cur;
        }
        return ans;
    }
}
