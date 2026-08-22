// LeetCode 3439 - Reschedule Meetings for Maximum Free Time I
// https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/

#include <stdlib.h>

int maxFreeTime(int eventTime, int k, int* startTime, int startTimeSize, int* endTime, int endTimeSize) {
    (void)endTimeSize;
    int n = startTimeSize;
    int* gaps = (int*)malloc((n + 1) * sizeof(int));
    gaps[0] = startTime[0];
    for (int i = 1; i < n; i++) gaps[i] = startTime[i] - endTime[i - 1];
    gaps[n] = eventTime - endTime[n - 1];
    int window = k + 1, sum = 0;
    for (int i = 0; i < window && i <= n; i++) sum += gaps[i];
    int ans = sum;
    for (int i = window; i <= n; i++) {
        sum += gaps[i] - gaps[i - window];
        if (sum > ans) ans = sum;
    }
    free(gaps);
    return ans;
}
