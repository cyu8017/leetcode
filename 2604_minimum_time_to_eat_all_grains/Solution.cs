// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

using System;

public class Solution {
    public int MinimumTime(int[] hens, int[] grains) {
        Array.Sort(hens);
        Array.Sort(grains);
        bool Ok(int t) {
            int j = 0;
            foreach (int h in hens) {
                if (j >= grains.Length) return true;
                if (grains[j] >= h) {
                    while (j < grains.Length && grains[j] - h <= t) j++;
                } else {
                    if (h - grains[j] > t) return false;
                    int left = h - grains[j];
                    int maxRight1 = t - 2 * left;
                    int maxRight2 = (t - left) / 2;
                    int reach = h;
                    if (maxRight1 > maxRight2) {
                        if (maxRight1 > 0) reach = h + maxRight1;
                    } else {
                        if (maxRight2 > 0) reach = h + maxRight2;
                    }
                    while (j < grains.Length && grains[j] <= reach) j++;
                }
            }
            return j >= grains.Length;
        }
        int lo = 0, hi = 2000000000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
