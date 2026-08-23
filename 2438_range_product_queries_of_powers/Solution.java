// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] productQueries(int n, int[][] queries) {
        final int mod = 1000000007;
        var powers = new ArrayList<Integer>();
        for (int bit = 0; bit < 31; bit++) {
            if (((n >> bit) & 1) != 0) powers.add(1 << bit);
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long prod = 1;
            for (int j = queries[i][0]; j <= queries[i][1]; j++)
                prod = prod * powers.get(j) % mod;
            ans[i] = (int)prod;
        }
        return ans;
    }
}
