// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

using System;
using System.Collections.Generic;

public class Solution {
    public long MakeSubKSumEqual(int[] arr, int k) {
        int n = arr.Length;
        int g = Gcd(n, k);
        long ans = 0;
        for (int r = 0; r < g; ++r) {
            var group = new List<int>();
            for (int i = r; i < n; i += g) group.Add(arr[i]);
            group.Sort();
            int med = group[group.Count / 2];
            foreach (int x in group) ans += Math.Abs(x - med);
        }
        return ans;
    }

    int Gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
