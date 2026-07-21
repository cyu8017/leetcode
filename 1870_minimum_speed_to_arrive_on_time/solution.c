// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

#include <stdbool.h>

static bool canArrive(int* dist, int distSize, int speed, double hour) {
    double time = 0.0;
    for (int i = 0; i < distSize - 1; i++) {
        time += (dist[i] + speed - 1) / speed;
    }
    time += (double)dist[distSize - 1] / speed;
    return time <= hour;
}

int minSpeedOnTime(int* dist, int distSize, double hour) {
    if (distSize - 1 >= hour) return -1;
    if (!canArrive(dist, distSize, 10000000, hour)) return -1;
    int lo = 1, hi = 10000000;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canArrive(dist, distSize, mid, hour)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
