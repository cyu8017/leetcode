// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

class Solution {
    public double equalizeWater(int[] buckets, int loss) {
        double lo = 0, hi = 0;
        for (int b : buckets) hi = Math.max(hi, (double) b);
        for (int iter = 0; iter < 60; iter++) {
            double mid = (lo + hi) / 2;
            double have = 0, need = 0;
            for (int b : buckets) {
                if (b >= mid) have += b - mid;
                else need += mid - b;
            }
            if (have * (1.0 - loss / 100.0) >= need) lo = mid;
            else hi = mid;
        }
        return lo;
    }
}
