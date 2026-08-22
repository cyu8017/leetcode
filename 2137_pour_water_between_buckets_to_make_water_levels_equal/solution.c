// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

double equalizeWater(int* buckets, int bucketsSize, int loss) {
    double lo = 0.0, hi = 0.0;
    for (int i = 0; i < bucketsSize; i++) if ((double)buckets[i] > hi) hi = (double)buckets[i];
    for (int iter = 0; iter < 60; iter++) {
        double mid = (lo + hi) / 2.0;
        double have = 0.0, need = 0.0;
        for (int i = 0; i < bucketsSize; i++) {
            if ((double)buckets[i] >= mid) have += (double)buckets[i] - mid;
            else need += mid - (double)buckets[i];
        }
        if (have * (1.0 - (double)loss / 100.0) >= need) lo = mid;
        else hi = mid;
    }
    return lo;
}
