// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/
// JS-only problem; C# stand-in with nullable placeholders as int.MinValue sentinel.

using System;
using System.Collections.Generic;

public class Solution {
    public Func<int[], int> Partial(Func<int[], int> fn, int[] args) {
        return rest => {
            var full = new List<int>();
            int ri = 0;
            foreach (int a in args) {
                if (a == int.MinValue) {
                    if (ri < rest.Length) full.Add(rest[ri++]);
                } else {
                    full.Add(a);
                }
            }
            while (ri < rest.Length) full.Add(rest[ri++]);
            return fn(full.ToArray());
        };
    }
}
