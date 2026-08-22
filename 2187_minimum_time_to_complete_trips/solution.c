// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

long long minimumTime(int* time, int timeSize, int totalTrips) {
    int mn = time[0];
    for (int i = 0; i < timeSize; i++) if (time[i] < mn) mn = time[i];
    long long lo = 1, hi = (long long)mn * totalTrips;
    while (lo < hi) {
        long long mid = (lo + hi) / 2, trips = 0;
        int ok = 0;
        for (int i = 0; i < timeSize; i++) {
            trips += mid / time[i];
            if (trips >= totalTrips) { ok = 1; break; }
        }
        if (ok) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
