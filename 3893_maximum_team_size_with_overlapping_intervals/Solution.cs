// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

using System;

public class Solution {
    public int MaximumTeamSize(int[] startTime, int[] endTime) {
        int n = startTime.Length;
        var st = (int[])startTime.Clone();
        var en = (int[])endTime.Clone();
        Array.Sort(st);
        Array.Sort(en);
        int ans = 0;
        for (int t = 0; t < n; t++) {
            int l = startTime[t], r = endTime[t];
            int i = UpperBound(en, l - 1);
            int j = UpperBound(st, r);
            ans = Math.Max(ans, j - i);
        }
        return ans;
    }
    static int UpperBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
