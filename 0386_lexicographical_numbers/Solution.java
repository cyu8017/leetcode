// LeetCode 0386 - Lexicographical Numbers

// https://leetcode.com/problems/lexicographical-numbers/



import java.util.ArrayList;

import java.util.List;



class Solution {

    public List<Integer> lexicalOrder(int n) {

        List<Integer> result = new ArrayList<>();

        dfs(1, n, result);

        return result;

    }



    private void dfs(int current, int n, List<Integer> result) {

        if (current > n) {

            return;

        }

        result.add(current);

        dfs(current * 10, n, result);

        if (current % 10 < 9) {

            dfs(current + 1, n, result);

        }

    }

}
