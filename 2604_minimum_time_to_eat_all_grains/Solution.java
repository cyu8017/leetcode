// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

import java.util.Arrays;

class Solution {
    public int minimumTime(int[] hens, int[] grains) {
        Arrays.sort(hens);
        Arrays.sort(grains);
        int lo = 0, hi = 2_000_000_000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (ok(hens, grains, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean ok(int[] hens, int[] grains, int t) {
        int j = 0;
        for (int h : hens) {
            if (j >= grains.length) return true;
            if (grains[j] >= h) {
                while (j < grains.length && grains[j] - h <= t) j++;
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
                while (j < grains.length && grains[j] <= reach) j++;
            }
        }
        return j >= grains.length;
    }
}
