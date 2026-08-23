// LeetCode 2427 - Number of Common Factors
// https://leetcode.com/problems/number-of-common-factors/

using System;

public class Solution {
    public int CommonFactors(int a, int b) {
        int g = Gcd(a, b);
        int ans = 0;
        for (int i = 1; i * i <= g; i++) {
            if (g % i == 0) {
                ans++;
                if (i * i != g) ans++;
            }
        }
        return ans;
    }

    private int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
