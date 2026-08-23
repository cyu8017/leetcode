// LeetCode 2975 - Maximum Square Area by Removing Fences From a Field
// https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        const int mod = 1000000007;
        HashSet<int> Gaps(int[] fences, int bound) {
            var list = new List<int>(fences) { 1, bound };
            list.Sort();
            var gaps = new HashSet<int>();
            for (int i = 0; i < list.Count; i++)
                for (int j = i + 1; j < list.Count; j++)
                    gaps.Add(list[j] - list[i]);
            return gaps;
        }
        var hg = Gaps(hFences, m);
        var vg = Gaps(vFences, n);
        long best = -1;
        foreach (int g in hg) {
            if (vg.Contains(g) && g > best) best = g;
        }
        if (best < 0) return -1;
        return (int)(best * best % mod);
    }
}
