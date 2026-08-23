// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private long modPow(long a, long b, long mod) {
        long res = 1 % mod;
        a %= mod;
        while (b > 0) {
            if ((b & 1) != 0) res = res * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return res;
    }

    public List<Integer> getGoodIndices(int[][] variables, int target) {
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < variables.length; i++) {
            int[] v = variables[i];
            int a = v[0], b = v[1], c = v[2], m = v[3];
            if (modPow(modPow(a, b, 10), c, m) == target) ans.add(i);
        }
        return ans;
    }
}
