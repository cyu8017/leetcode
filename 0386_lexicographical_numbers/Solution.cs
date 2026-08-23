// LeetCode 0386 - Lexicographical Numbers

// https://leetcode.com/problems/lexicographical-numbers/



using System.Collections.Generic;



public class Solution {

    public IList<int> LexicalOrder(int n) {

        List<int> result = new List<int>();

        Dfs(1, n, result);

        return result;

    }



    private void Dfs(int current, int n, List<int> result) {

        if (current > n) {

            return;

        }

        result.Add(current);

        Dfs(current * 10, n, result);

        if (current % 10 < 9) {

            Dfs(current + 1, n, result);

        }

    }

}
