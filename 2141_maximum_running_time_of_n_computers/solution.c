// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

long long maxRunTime(int n, int* batteries, int batteriesSize) {
    long long sum = 0;
    for (int i = 0; i < batteriesSize; i++) sum += batteries[i];
    long long lo = 1, hi = sum / n;
    while (lo < hi) {
        long long mid = (lo + hi + 1) / 2;
        long long need = 0;
        for (int i = 0; i < batteriesSize; i++)
            need += batteries[i] > mid ? mid : batteries[i];
        if (need >= mid * n) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
