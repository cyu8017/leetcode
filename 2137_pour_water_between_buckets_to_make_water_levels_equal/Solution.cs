// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

public class Solution {
    public double EqualizeWater(int[] buckets, int loss) {
        double lo = 0, hi = 0;
        foreach (int b in buckets) hi = Math.Max(hi, (double)b);
        bool Can(double x) {
            double have = 0, need = 0;
            foreach (int b in buckets) {
                if (b >= x) have += b - x;
                else need += x - b;
            }
            return have * (1.0 - loss / 100.0) >= need;
        }
        for (int iter = 0; iter < 60; iter++) {
            double mid = (lo + hi) / 2;
            if (Can(mid)) lo = mid;
            else hi = mid;
        }
        return lo;
    }
}
