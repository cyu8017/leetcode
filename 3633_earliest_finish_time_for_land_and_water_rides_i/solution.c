// LeetCode 3633 - Earliest Finish Time for Land and Water Rides I
// https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/

#include <limits.h>
static int imin(int a,int b){return a<b?a:b;}
static int imax(int a,int b){return a>b?a:b;}
static int calc(int* a1, int n1, int* t1, int* a2, int n2, int* t2) {
    int minEnd = INT_MAX;
    for (int i = 0; i < n1; i++) minEnd = imin(minEnd, a1[i] + t1[i]);
    int ans = INT_MAX;
    for (int i = 0; i < n2; i++) ans = imin(ans, imax(minEnd, a2[i]) + t2[i]);
    return ans;
}
int earliestFinishTime(int* landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize, int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize) {
    (void)landDurationSize;(void)waterDurationSize;
    int x = calc(landStartTime, landStartTimeSize, landDuration, waterStartTime, waterStartTimeSize, waterDuration);
    int y = calc(waterStartTime, waterStartTimeSize, waterDuration, landStartTime, landStartTimeSize, landDuration);
    return imin(x, y);
}
