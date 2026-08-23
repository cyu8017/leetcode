// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

// JS cancellable generator stand-in
using System;

public class Solution {
    public (Action cancel, Func<(int, bool)> run) Cancellable(Func<int> generator) {
        bool cancelled = false;
        bool done = false;
        int result = 0;
        Action cancel = () => { cancelled = true; };
        Func<(int, bool)> run = () => {
            if (done) return (result, true);
            result = generator();
            done = true;
            return (result, !cancelled);
        };
        return (cancel, run);
    }
}
