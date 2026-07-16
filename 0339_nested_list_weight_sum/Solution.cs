// LeetCode 0339 - Nested List Weight Sum

// https://leetcode.com/problems/nested-list-weight-sum/



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

        return Dfs(nestedList, 1);

    }



    private int Dfs(IList<NestedInteger> items, int depth) {

        int total = 0;

        foreach (NestedInteger item in items) {

            if (item.IsInteger()) {

                total += item.GetInteger() * depth;

            } else {

                total += Dfs(item.GetList(), depth + 1);

            }

        }

        return total;

    }

}
