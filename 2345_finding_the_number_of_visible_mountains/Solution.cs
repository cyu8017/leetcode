// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

using System;
using System.Collections.Generic;

public class Solution {
    public int VisibleMountains(int[][] peaks) {
        var arr = new List<(int l, int r)>();
        foreach (var p in peaks) arr.Add((p[0] - p[1], p[0] + p[1]));
        arr.Sort((a, b) => {
            if (a.l == b.l) return b.r.CompareTo(a.r);
            return a.l.CompareTo(b.l);
        });
        int ans = 0;
        int maxR = int.MinValue;
        for (int i = 0; i < arr.Count; ) {
            int j = i;
            while (j < arr.Count && arr[j].l == arr[i].l && arr[j].r == arr[i].r) j++;
            if (arr[i].r > maxR) {
                if (j - i == 1) ans++;
                maxR = arr[i].r;
            }
            i = j;
        }
        return ans;
    }
}
