// LeetCode 0339 - Nested List Weight Sum

// https://leetcode.com/problems/nested-list-weight-sum/



import java.util.ArrayList;

import java.util.List;



class NestedInteger {

    private Integer integer;

    private final List<NestedInteger> list = new ArrayList<>();



    public NestedInteger() {}



    public NestedInteger(int value) {

        this.integer = value;

    }



    public boolean isInteger() {

        return integer != null;

    }



    public int getInteger() {

        return integer != null ? integer : 0;

    }



    public List<NestedInteger> getList() {

        return list;

    }

}



class Solution {

    public int depthSum(List<NestedInteger> nestedList) {

        return dfs(nestedList, 1);

    }



    private int dfs(List<NestedInteger> items, int depth) {

        int total = 0;

        for (NestedInteger item : items) {

            if (item.isInteger()) {

                total += item.getInteger() * depth;

            } else {

                total += dfs(item.getList(), depth + 1);

            }

        }

        return total;

    }

}
