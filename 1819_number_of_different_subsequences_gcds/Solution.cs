// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

using System;

public class Solution {
    public int CountDifferentSubsequenceGCDs(int[] nums) {
        int maxVal = 0;
        foreach (int num in nums) maxVal = Math.Max(maxVal, num);
        bool[] present = new bool[maxVal + 1];
        foreach (int num in nums) present[num] = true;

        int ans = 0;
        for (int g = 1; g <= maxVal; g++) {
            int gcdVal = 0;
            bool has = false;
            for (int multiple = g; multiple <= maxVal; multiple += g) {
                if (!present[multiple]) continue;
                has = true;
                gcdVal = Gcd(gcdVal, multiple / g);
                if (gcdVal == 1) break;
            }
            if (has && gcdVal == 1) ans++;
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
