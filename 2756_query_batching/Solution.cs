// LeetCode 2756 - Query Batching
// https://leetcode.com/problems/query-batching/
// JS QueryBatcher design stand-in.

using System;
using System.Collections.Generic;

public class QueryBatcher {
    private readonly Func<int[], int[]> queryMultiple;
    private readonly int t;
    private readonly List<int> pending = new List<int>();
    private readonly List<Action<int>> resolvers = new List<Action<int>>();

    public QueryBatcher(Func<int[], int[]> queryMultiple, int t) {
        this.queryMultiple = queryMultiple;
        this.t = t;
    }

    public void AddQuery(int query, Action<int> resolve) {
        pending.Add(query);
        resolvers.Add(resolve);
    }
}
