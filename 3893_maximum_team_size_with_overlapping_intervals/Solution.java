// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

import java.util.Arrays;

class Solution {
    public int maximumTeamSize(int[] startTime, int[] endTime) {
        int n = startTime.length;
        var st = startTime.clone();
        var en = endTime.clone();
        Arrays.sort(st);
        Arrays.sort(en);
        int ans = 0;
        for (int t = 0; t < n; t++) {
            int l = startTime[t], r = endTime[t];
            int i = UpperBound(en, l - 1);
            int j = UpperBound(st, r);
            ans = Math.max(ans, j - i);
        }
        return ans;
    }
    static int UpperBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
