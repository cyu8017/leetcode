// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        int n = dist.length;
        if (n - 1 >= hour) {
            return -1;
        }

        if (!canArrive(dist, hour, 10_000_000)) {
            return -1;
        }

        int lo = 1;
        int hi = 10_000_000;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (canArrive(dist, hour, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }

    private boolean canArrive(int[] dist, double hour, int speed) {
        double time = 0.0;
        for (int i = 0; i < dist.length - 1; i++) {
            time += (dist[i] + speed - 1) / speed;
        }
        time += (double) dist[dist.length - 1] / speed;
        return time <= hour;
    }
}
