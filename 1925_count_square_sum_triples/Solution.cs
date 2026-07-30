// LeetCode 1925 - Count Square Sum Triples
// https://leetcode.com/problems/count-square-sum-triples/

using System.Collections.Generic;

public class Solution {
    public int CountTriples(int n) {
        var squares = new HashSet<int>();
        for (int i = 1; i <= n; i++) squares.Add(i * i);
        int ans = 0;
        for (int a = 1; a <= n; a++)
            for (int b = 1; b <= n; b++)
                if (squares.Contains(a * a + b * b)) ans++;
        return ans;
    }
}