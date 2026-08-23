// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths, string directions) {
        int n = positions.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => positions[a].CompareTo(positions[b]));
        var stack = new List<(int i, int h, char d)>();
        foreach (int i in idx) {
            var cur = (i, h: healths[i], d: directions[i]);
            while (stack.Count > 0 && stack[^1].d == 'R' && cur.d == 'L') {
                if (stack[^1].h == cur.h) {
                    stack.RemoveAt(stack.Count - 1);
                    cur.h = 0;
                    break;
                } else if (stack[^1].h > cur.h) {
                    var top = stack[^1];
                    top.h--;
                    stack[^1] = top;
                    cur.h = 0;
                    break;
                } else {
                    cur.h--;
                    stack.RemoveAt(stack.Count - 1);
                }
            }
            if (cur.h > 0) stack.Add(cur);
        }
        var alive = new Dictionary<int, int>();
        foreach (var r in stack) alive[r.i] = r.h;
        var ans = new List<int>();
        for (int i = 0; i < n; i++)
            if (alive.ContainsKey(i)) ans.Add(alive[i]);
        return ans;
    }
}
