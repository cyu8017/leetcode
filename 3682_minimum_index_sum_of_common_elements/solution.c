// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

#include <string.h>

#define MAP_SIZE 200003
static int mk[MAP_SIZE], mv[MAP_SIZE];
static char mu[MAP_SIZE];

int minimumSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    memset(mu, 0, sizeof(mu));
    for (int i = 0; i < nums2Size; i++) {
        int k = nums2[i];
        int idx = (int)((unsigned)k % MAP_SIZE);
        while (mu[idx] && mk[idx] != k) { if (++idx == MAP_SIZE) idx = 0; }
        if (!mu[idx]) { mu[idx] = 1; mk[idx] = k; mv[idx] = i; }
    }
    const int inf = 1 << 30;
    int ans = inf;
    for (int i = 0; i < nums1Size; i++) {
        int k = nums1[i];
        int idx = (int)((unsigned)k % MAP_SIZE);
        while (mu[idx] && mk[idx] != k) { if (++idx == MAP_SIZE) idx = 0; }
        if (mu[idx] && mk[idx] == k) {
            int s = i + mv[idx];
            if (s < ans) ans = s;
        }
    }
    return ans == inf ? -1 : ans;
}
