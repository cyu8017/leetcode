// LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

#include <stdlib.h>
#include <limits.h>

static int abs3171(int x) { return x < 0 ? -x : x; }

int minimumDifference(int* nums, int numsSize, int k) {
    int mx = nums[0];
    for (int i = 1; i < numsSize; i++) if (nums[i] > mx) mx = nums[i];
    int m = 0;
    unsigned u = (unsigned)mx;
    while (u) { m++; u >>= 1; }
    if (m == 0) m = 1;
    int* cnt = calloc(m, sizeof(int));
    int ans = INT_MAX, s = 0, i = 0;
    for (int j = 0; j < numsSize; j++) {
        int x = nums[j];
        s |= x;
        int d = abs3171(s - k); if (d < ans) ans = d;
        for (int h = 0; h < m; h++) if ((x >> h) & 1) cnt[h]++;
        while (i < j && s > k) {
            int y = nums[i];
            for (int h = 0; h < m; h++) {
                if ((y >> h) & 1) {
                    cnt[h]--;
                    if (cnt[h] == 0) s ^= 1 << h;
                }
            }
            d = abs3171(s - k); if (d < ans) ans = d;
            i++;
        }
    }
    free(cnt);
    return ans;
}
