// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

public class Solution {
    public double MinmaxGasDist(int[] stations, int k) {
        bool Can(double dist) {
            int needed = 0;
            for (int i = 1; i < stations.Length; i++)
                needed += (int)((stations[i] - stations[i - 1]) / dist);
            return needed <= k;
        }
        double lo = 0.0, hi = stations[stations.Length - 1] - stations[0];
        while (hi - lo > 1e-6) {
            double mid = (lo + hi) / 2.0;
            if (Can(mid)) hi = mid;
            else lo = mid;
        }
        return hi;
    }
}
