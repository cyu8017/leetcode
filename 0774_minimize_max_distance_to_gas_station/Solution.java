// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution {
    public double minmaxGasDist(int[] stations, int k) {
        double lo = 0.0, hi = stations[stations.length - 1] - stations[0];
        while (hi - lo > 1e-6) {
            double mid = (lo + hi) / 2.0;
            if (can(stations, k, mid)) hi = mid;
            else lo = mid;
        }
        return hi;
    }

    private boolean can(int[] stations, int k, double dist) {
        int needed = 0;
        for (int i = 1; i < stations.length; i++)
            needed += (int) ((stations[i] - stations[i - 1]) / dist);
        return needed <= k;
    }
}
