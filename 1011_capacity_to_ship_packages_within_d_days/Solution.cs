// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

using System.Linq;

public class Solution {
    public int ShipWithinDays(int[] weights, int days) {
        int lo = weights.Max(), hi = weights.Sum();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Can(weights, days, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private static bool Can(int[] weights, int days, int cap) {
        int need = 1, cur = 0;
        foreach (int w in weights) {
            if (cur + w > cap) {
                need++;
                cur = 0;
            }
            cur += w;
        }
        return need <= days;
    }
}
