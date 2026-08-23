// LeetCode 2795 - Parallel Execution of Promises for Individual Results Retrieval
// https://leetcode.com/problems/parallel-execution-of-promises-for-individual-results-retrieval/
// JS-only problem; C# stand-in.

using System;
using System.Collections.Generic;

public class Solution {
    public IList<(string, int)> PromiseAllSettled(IList<Func<int>> functions) {
        var ans = new List<(string, int)>();
        foreach (var f in functions) ans.Add(("fulfilled", f()));
        return ans;
    }
}
