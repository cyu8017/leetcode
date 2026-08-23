// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

using System.Collections.Generic;

public class Solution {
    public bool BuddyStrings(string s, string goal) {
        if (s.Length != goal.Length) return false;
        if (s == goal) return new HashSet<char>(s).Count < s.Length;
        var diffs = new List<(char a, char b)>();
        for (int i = 0; i < s.Length; i++)
            if (s[i] != goal[i]) diffs.Add((s[i], goal[i]));
        return diffs.Count == 2 && diffs[0].a == diffs[1].b && diffs[0].b == diffs[1].a;
    }
}
