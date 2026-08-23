// LeetCode 2721 - Execute Asynchronous Functions in Parallel
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/

// JS promiseAll stand-in: run sync functions in order
using System;
using System.Collections.Generic;

public class Solution {
    public int[] PromiseAll(IList<Func<int>> functions) {
        var outList = new List<int>();
        foreach (var f in functions) outList.Add(f());
        return outList.ToArray();
    }
}
