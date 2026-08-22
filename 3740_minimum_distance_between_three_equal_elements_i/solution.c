// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

#include <stdlib.h>
#include <string.h>

#define MAP_SIZE 200003
static int mk[MAP_SIZE];
static int* ml[MAP_SIZE];
static int mn[MAP_SIZE], mcap[MAP_SIZE];
static char mu[MAP_SIZE];

static void mc(void) {
    for (int i = 0; i < MAP_SIZE; i++) if (mu[i]) { free(ml[i]); mu[i]=0; mn[i]=0; mcap[i]=0; }
}

static void madd(int k, int idx) {
    int i = (int)((unsigned)k % MAP_SIZE);
    while (mu[i] && mk[i] != k) { if (++i == MAP_SIZE) i = 0; }
    if (!mu[i]) { mu[i]=1; mk[i]=k; ml[i]=NULL; mn[i]=0; mcap[i]=0; }
    if (mn[i] == mcap[i]) {
        mcap[i] = mcap[i] ? mcap[i]*2 : 4;
        ml[i] = (int*)realloc(ml[i], (size_t)mcap[i]*sizeof(int));
    }
    ml[i][mn[i]++] = idx;
}

int minimumDistance(int* nums, int numsSize) {
    mc();
    for (int i = 0; i < numsSize; i++) madd(nums[i], i);
    int inf = 1 << 30, ans = inf;
    for (int i = 0; i < MAP_SIZE; i++) {
        if (!mu[i]) continue;
        int m = mn[i];
        for (int h = 0; h < m - 2; h++) {
            int t = (ml[i][h + 2] - ml[i][h]) * 2;
            if (t < ans) ans = t;
        }
    }
    mc();
    return ans == inf ? -1 : ans;
}
