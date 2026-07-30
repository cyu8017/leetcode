// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> BeforeAndAfterPuzzles(string[] phrases) {
        var split = phrases.Select(p => p.Split(' ')).ToArray();
        var result = new HashSet<string>();
        for (int i = 0; i < split.Length; i++) {
            for (int j = 0; j < split.Length; j++) {
                if (i == j) continue;
                if (split[i][^1] == split[j][0]) {
                    var parts = new List<string>(split[i]);
                    parts.AddRange(split[j].Skip(1));
                    result.Add(string.Join(" ", parts));
                }
            }
        }
        return result.OrderBy(x => x).ToList();
    }
}
