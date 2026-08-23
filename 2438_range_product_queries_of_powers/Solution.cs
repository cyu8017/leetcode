// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

using System.Collections.Generic;

public class Solution {
    public int[] ProductQueries(int n, int[][] queries) {
        const int mod = 1000000007;
        var powers = new List<int>();
        for (int bit = 0; bit < 31; bit++) {
            if (((n >> bit) & 1) != 0) powers.Add(1 << bit);
        }
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            long prod = 1;
            for (int j = queries[i][0]; j <= queries[i][1]; j++)
                prod = prod * powers[j] % mod;
            ans[i] = (int)prod;
        }
        return ans;
    }
}
