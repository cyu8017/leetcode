// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int lo = 0, hi = 0;
        for (int w : weights) {
            lo = Math.max(lo, w);
            hi += w;
        }
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (can(weights, days, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean can(int[] weights, int days, int cap) {
        int need = 1, cur = 0;
        for (int w : weights) {
            if (cur + w > cap) {
                need++;
                cur = 0;
            }
            cur += w;
        }
        return need <= days;
    }
}
