// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

// JS throttle stand-in: calls fn at most once per t ms (wall clock)
using System;
using System.Diagnostics;

public class Solution {
    public Action Throttle(Action fn, int t) {
        var sw = Stopwatch.StartNew();
        long last = -24L * 3600 * 1000;
        return () => {
            long now = sw.ElapsedMilliseconds;
            if (now - last >= t) {
                last = now;
                fn();
            }
        };
    }
}
