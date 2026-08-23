// LeetCode 3266 - Final Array State After K Multiplication Operations II
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

using System;
using System.Collections.Generic;

public class Solution {
    long ModPow(long a, long e, long mod) {
        long r = 1;
        a %= mod;
        while (e > 0) {
            if ((e & 1) != 0) r = r * a % mod;
            a = a * a % mod;
            e >>= 1;
        }
        return r;
    }

    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        const int mod = 1000000007;
        if (multiplier == 1) return nums;
        var h = new PriorityQueue<int, (int, int)>();
        int maxV = 0;
        for (int i = 0; i < nums.Length; i++) {
            h.Enqueue(i, (nums[i], i));
            if (nums[i] > maxV) maxV = nums[i];
        }
        while (k > 0 && h.Count > 0) {
            int i = h.Dequeue();
            int v = nums[i];
            if ((long)v * multiplier > maxV && k >= nums.Length) {
                h.Enqueue(i, (v, i));
                break;
            }
            int nv = v * multiplier;
            nums[i] = nv;
            if (nv > maxV) maxV = nv;
            h.Enqueue(i, (nv, i));
            k--;
        }
        if (k > 0) {
            int n = nums.Length;
            int full = k / n, rem = k % n;
            long powFull = ModPow(multiplier, full, mod);
            for (int i = 0; i < n; i++) nums[i] = (int)((long)nums[i] * powFull % mod);
            var hh = new PriorityQueue<int, (int, int)>();
            for (int i = 0; i < n; i++) hh.Enqueue(i, (nums[i], i));
            for (int t = 0; t < rem; t++) {
                int i = hh.Dequeue();
                int v = (int)((long)nums[i] * multiplier % mod);
                nums[i] = v;
                hh.Enqueue(i, (v, i));
            }
            for (int i = 0; i < n; i++) nums[i] %= mod;
        } else {
            for (int i = 0; i < nums.Length; i++) nums[i] %= mod;
        }
        return nums;
    }
}
