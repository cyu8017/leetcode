// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string[] ReorderLogFiles(string[] logs) {
        var letter = new List<(string log, string rest, string id, int idx)>();
        var digit = new List<(string log, int idx)>();
        for (int i = 0; i < logs.Length; i++) {
            int sp = logs[i].IndexOf(' ');
            string rest = logs[i].Substring(sp + 1);
            if (char.IsLetter(rest[0])) letter.Add((logs[i], rest, logs[i].Substring(0, sp), i));
            else digit.Add((logs[i], i));
        }
        letter = letter.OrderBy(x => x.rest, StringComparer.Ordinal)
            .ThenBy(x => x.id, StringComparer.Ordinal).ToList();
        var ans = new List<string>();
        foreach (var x in letter) ans.Add(x.log);
        foreach (var x in digit) ans.Add(x.log);
        return ans.ToArray();
    }
}
