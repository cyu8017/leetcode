// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimumJumps(int[] forbidden, int a, int b, int x) {
        var bad = new HashSet<int>(forbidden);
        int limit = Math.Max(x, forbidden.DefaultIfEmpty(0).Max()) + a + b;
        var q = new Queue<(int pos, int dist, bool back)>();
        var seen = new HashSet<(int, bool)>();
        q.Enqueue((0, 0, false));
        seen.Add((0, false));
        while (q.Count > 0) {
            var (p, d, back) = q.Dequeue();
            if (p == x) return d;
            foreach (var (np, nb) in new[] { (p + a, false), (p - b, true) }) {
                if (np < 0 || np > limit || bad.Contains(np) || seen.Contains((np, nb))) continue;
                if (back && nb) continue;
                seen.Add((np, nb));
                q.Enqueue((np, d + 1, nb));
            }
        }
        return -1;
    }
}
