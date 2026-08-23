// LeetCode 0364 - Nested List Weight Sum II

// https://leetcode.com/problems/nested-list-weight-sum-ii/



using System.Collections.Generic;



public class NestedInteger {

    private int? integer;

    private readonly List<NestedInteger> list = new();



    public NestedInteger() {}



    public NestedInteger(int value) {

        integer = value;

    }



    public bool IsInteger() {

        return integer.HasValue;

    }



    public int GetInteger() {

        return integer ?? 0;

    }



    public IList<NestedInteger> GetList() {

        return list;

    }

}



public class Solution {

    public int DepthSum(IList<NestedInteger> nestedList) {

        List<(int value, int depth)> weighted = new();

        Dfs(nestedList, 1, weighted);

        if (weighted.Count == 0) {

            return 0;

        }



        int maxDepth = 0;

        foreach ((_, int depth) in weighted) {

            maxDepth = Math.Max(maxDepth, depth);

        }



        int total = 0;

        foreach ((int value, int depth) in weighted) {

            total += value * (maxDepth - depth + 1);

        }

        return total;

    }



    private void Dfs(IList<NestedInteger> items, int depth, List<(int value, int depth)> weighted) {

        foreach (NestedInteger item in items) {

            if (item.IsInteger()) {

                weighted.Add((item.GetInteger(), depth));

            } else {

                Dfs(item.GetList(), depth + 1, weighted);

            }

        }

    }

}
