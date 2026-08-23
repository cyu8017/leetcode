// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

// JS interval cancellation stand-in
using System;
using System.Collections.Generic;

public class Solution {
    public (Action cancel, int[] results) Cancellable(Func<int> fn, int t, int times) {
        bool cancelled = false;
        var results = new List<int>();
        for (int i = 0; i < times && !cancelled; i++) results.Add(fn());
        Action cancel = () => { cancelled = true; };
        return (cancel, results.ToArray());
    }
}
