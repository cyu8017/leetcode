// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

// JavaScript problem; C# stand-in.
using System;
using System.Collections.Generic;

public class Solution {
    public Func<int, int> Compose(IList<Func<int, int>> functions) {
        return x => {
            for (int i = functions.Count - 1; i >= 0; i--) x = functions[i](x);
            return x;
        };
    }
}
