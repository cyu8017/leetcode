// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinGenerations(int[][] points, int[] target) {
        var targetPoint = (target[0], target[1], target[2]);
        var generation = new Dictionary<(int, int, int), int>();
        var all = new List<(int, int, int)>();
        foreach (var values in points) {
            var p = (values[0], values[1], values[2]);
            generation[p] = 0;
            all.Add(p);
        }
        if (generation.ContainsKey(targetPoint)) return generation[targetPoint];
        for (int current = 1; ; current++) {
            int limit = all.Count;
            var added = new List<(int, int, int)>();
            for (int i = 0; i < limit; i++) {
                for (int j = i + 1; j < limit; j++) {
                    if (all[i].Equals(all[j])) continue;
                    var p = (
                        (all[i].Item1 + all[j].Item1) / 2,
                        (all[i].Item2 + all[j].Item2) / 2,
                        (all[i].Item3 + all[j].Item3) / 2
                    );
                    if (!generation.ContainsKey(p)) {
                        generation[p] = current;
                        added.Add(p);
                    }
                }
            }
            if (generation.ContainsKey(targetPoint)) return generation[targetPoint];
            if (added.Count == 0) return -1;
            all.AddRange(added);
        }
    }
}
