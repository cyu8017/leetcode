// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] FullBloomFlowers(int[][] flowers, int[] people) {
        var start = new List<int>();
        var end = new List<int>();
        foreach (var f in flowers) { start.Add(f[0]); end.Add(f[1]); }
        start.Sort();
        end.Sort();
        int[] ans = new int[people.Length];
        for (int i = 0; i < people.Length; i++) {
            int t = people[i];
            int started = UpperBound(start, t);
            int ended = LowerBound(end, t);
            ans[i] = started - ended;
        }
        return ans;
    }

    static int UpperBound(List<int> a, int t) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    static int LowerBound(List<int> a, int t) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
