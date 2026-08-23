// LeetCode 0364 - Nested List Weight Sum II

// https://leetcode.com/problems/nested-list-weight-sum-ii/



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

        List<int[]> weighted = new ArrayList<>();



        dfs(nestedList, 1, weighted);

        if (weighted.isEmpty()) {

            return 0;

        }



        int maxDepth = 0;

        for (int[] entry : weighted) {

            maxDepth = Math.max(maxDepth, entry[1]);

        }



        int total = 0;

        for (int[] entry : weighted) {

            total += entry[0] * (maxDepth - entry[1] + 1);

        }

        return total;

    }



    private void dfs(List<NestedInteger> items, int depth, List<int[]> weighted) {

        for (NestedInteger item : items) {

            if (item.isInteger()) {

                weighted.add(new int[] {item.getInteger(), depth});

            } else {

                dfs(item.getList(), depth + 1, weighted);

            }

        }

    }

}
