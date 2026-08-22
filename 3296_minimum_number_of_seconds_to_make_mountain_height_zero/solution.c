// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

static int ok3296(long long t, int mountainHeight, int* workerTimes, int workerTimesSize) {
    long long total = 0;
    for (int i = 0; i < workerTimesSize; i++) {
        long long w = workerTimes[i];
        long long lo = 0, hi = mountainHeight;
        while (lo < hi) {
            long long mid = (lo + hi + 1) / 2;
            if (w * mid * (mid + 1) / 2 <= t) lo = mid;
            else hi = mid - 1;
        }
        total += lo;
        if (total >= mountainHeight) return 1;
    }
    return total >= mountainHeight;
}

long long minNumberOfSeconds(int mountainHeight, int* workerTimes, int workerTimesSize) {
    long long lo = 0, hi = 1000000000000000000LL;
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        if (ok3296(mid, mountainHeight, workerTimes, workerTimesSize)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
