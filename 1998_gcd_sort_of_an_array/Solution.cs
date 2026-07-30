// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool GcdSort(int[] nums) {
        int m = nums.Max();
        var parent = Enumerable.Range(0, m + 1).ToArray();
        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        void Union(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra != rb) parent[rb] = ra;
        }
        var spf = Enumerable.Range(0, m + 1).ToArray();
        for (int i = 2; i * i <= m; i++) {
            if (spf[i] == i)
                for (int j = i * i; j <= m; j += i)
                    if (spf[j] == j) spf[j] = i;
        }
        foreach (int x in nums.Distinct()) {
            int y = x;
            while (y > 1) {
                int p = spf[y];
                Union(x, p);
                while (y % p == 0) y /= p;
            }
        }
        var sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        for (int i = 0; i < nums.Length; i++)
            if (Find(nums[i]) != Find(sorted[i])) return false;
        return true;
    }
}