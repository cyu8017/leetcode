// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

using System;
using System.Collections.Generic;

public class Solution {
    static int Cost(int x, int t) {
        if (x == t) return 0;
        if (x % t == 0 || t % x == 0) return 1;
        return 2;
    }

    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public int MinOperations(int[] nums) {
        int n = nums.Length;
        if (n <= 1) return 0;
        int g = nums[0], mn = nums[0];
        for (int i = 1; i < n; i++) {
            g = Gcd(g, nums[i]);
            mn = Math.Min(mn, nums[i]);
        }
        var cands = new HashSet<int>();
        foreach (int x in nums) cands.Add(x);
        for (int d = 1; 1L * d * d <= mn; d++) {
            if (mn % d == 0) {
                cands.Add(d);
                cands.Add(mn / d);
            }
        }
        cands.Add(g);
        int ans = int.MaxValue;
        foreach (int t in cands) {
            int sum = 0;
            foreach (int x in nums) {
                sum += Cost(x, t);
                if (sum >= ans) break;
            }
            ans = Math.Min(ans, sum);
        }
        return ans;
    }
}
