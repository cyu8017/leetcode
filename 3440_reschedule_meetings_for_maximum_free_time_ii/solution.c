// LeetCode 3440 - Reschedule Meetings for Maximum Free Time II
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/

#include <stdlib.h>

int maxFreeTime(int eventTime, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    (void)endTimeSize;
    int n = startTimeSize;
    int* gaps = (int*)malloc((n + 1) * sizeof(int));
    gaps[0] = startTime[0];
    for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    int ans = 0;
    for (int i = 0; i <= n; i++) if (gaps[i] > ans) ans = gaps[i];
    int* leftMax = (int*)malloc((n + 1) * sizeof(int));
    int* rightMax = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) { leftMax[i] = gaps[i]; if (i > 0 && leftMax[i - 1] > leftMax[i]) leftMax[i] = leftMax[i - 1]; }
    for (int i = n; i >= 0; i--) { rightMax[i] = gaps[i]; if (i < n && rightMax[i + 1] > rightMax[i]) rightMax[i] = rightMax[i + 1]; }
    for (int i = 0; i < n; i++) {
        int dur = endTime[i] - startTime[i];
        int merged = gaps[i] + gaps[i + 1];
        int bestOther = 0;
        if (i > 0 && leftMax[i - 1] > bestOther) bestOther = leftMax[i - 1];
        if (i + 2 <= n && rightMax[i + 2] > bestOther) bestOther = rightMax[i + 2];
        int cand = merged;
        if (bestOther >= dur) cand = merged + dur;
        if (cand > ans) ans = cand;
    }
    free(gaps); free(leftMax); free(rightMax);
    return ans;
}
