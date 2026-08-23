// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/
// JS-only problem; C# stand-in wrapping callables.

using System;
using System.Collections.Generic;

public class Solution {
    public IList<Func<int>> DelayAll(IList<Func<int>> functions, int ms) {
        return new List<Func<int>>(functions);
    }
}
