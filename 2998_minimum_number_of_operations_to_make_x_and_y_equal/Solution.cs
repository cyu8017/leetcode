// LeetCode 2998 - Minimum Number of Operations to Make X and Y Equal
// https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/

using System.Collections.Generic;

public class Solution {
    public int MinimumOperationsToMakeEqual(int x, int y) {
        if (x <= y) return y - x;
        var q = new Queue<(int v, int d)>();
        q.Enqueue((x, 0));
        var seen = new HashSet<int> { x };
        while (q.Count > 0) {
            var (v, d) = q.Dequeue();
            if (v == y) return d;
            var cands = new List<int> { v + 1, v - 1 };
            if (v % 11 == 0) cands.Add(v / 11);
            if (v % 5 == 0) cands.Add(v / 5);
            foreach (int nxt in cands) {
                if (nxt > 0 && nxt < 2 * x + 20 && seen.Add(nxt)) {
                    q.Enqueue((nxt, d + 1));
                }
            }
        }
        return -1;
    }
}
