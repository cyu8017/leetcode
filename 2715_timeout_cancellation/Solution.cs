// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

// JS timeout cancellation stand-in
using System;

public class Solution {
    public (Action cancel, Func<int?> result) Cancellable(Func<int> fn, int t) {
        bool cancelled = false;
        Action cancel = () => { cancelled = true; };
        Func<int?> result = () => {
            if (cancelled) return null;
            return fn();
        };
        return (cancel, result);
    }
}
