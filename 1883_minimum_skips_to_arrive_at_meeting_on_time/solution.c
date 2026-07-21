// LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

#include <stdlib.h>
#include <limits.h>

int minSkips(int* dist, int distSize, int speed, int hoursBefore) {
    long long limit = (long long)hoursBefore * speed;
    const long long INF = LLONG_MAX / 4;
    long long* dp = (long long*)malloc((size_t)(distSize + 1) * sizeof(long long));
    long long* nxt = (long long*)malloc((size_t)(distSize + 1) * sizeof(long long));
    for (int i = 0; i <= distSize; i++) dp[i] = INF;
    dp[0] = 0;
    for (int r = 0; r < distSize; r++) {
        int road = dist[r];
        for (int i = 0; i <= distSize; i++) nxt[i] = INF;
        for (int skips = 0; skips < distSize; skips++) {
            if (dp[skips] == INF) continue;
            long long rounded = ((dp[skips] + road + speed - 1) / speed) * speed;
            if (rounded < nxt[skips]) nxt[skips] = rounded;
            long long skipped = dp[skips] + road;
            if (skipped < nxt[skips + 1]) nxt[skips + 1] = skipped;
        }
        long long* tmp = dp;
        dp = nxt;
        nxt = tmp;
    }
    int answer = -1;
    for (int skips = 0; skips <= distSize; skips++) {
        if (dp[skips] <= limit) {
            answer = skips;
            break;
        }
    }
    free(dp);
    free(nxt);
    return answer;
}
