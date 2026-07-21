// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

public class Solution {
    public int MinSpeedOnTime(int[] dist, double hour) {
        int n = dist.Length;
        if (n - 1 >= hour) {
            return -1;
        }

        bool CanArrive(int speed) {
            double time = 0;
            for (int i = 0; i < n - 1; i++) {
                time += (dist[i] + speed - 1) / speed;
            }
            time += (double)dist[n - 1] / speed;
            return time <= hour;
        }

        if (!CanArrive(10_000_000)) {
            return -1;
        }
        int lo = 1;
        int hi = 10_000_000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (CanArrive(mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}
