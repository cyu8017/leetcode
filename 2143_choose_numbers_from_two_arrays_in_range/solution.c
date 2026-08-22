// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

#include <stdlib.h>
#include <string.h>

#define MOD2143 1000000007
#define OFF2143 20000
#define SZ2143 (OFF2143 * 2 + 5)

int countSubranges(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int* dp = (int*)calloc(SZ2143, sizeof(int));
    int* ndp = (int*)calloc(SZ2143, sizeof(int));
    int* keys = (int*)malloc(SZ2143 * sizeof(int));
    int* nkeys = (int*)malloc(SZ2143 * sizeof(int));
    int klen = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        memset(ndp, 0, SZ2143 * sizeof(int));
        int nlen = 0;
        #define ADD(diff, cnt) do { \
            int idx = (diff) + OFF2143; \
            if (ndp[idx] == 0) nkeys[nlen++] = diff; \
            ndp[idx] = (ndp[idx] + (cnt)) % MOD2143; \
        } while (0)
        ADD(nums1[i], 1);
        ADD(-nums2[i], 1);
        for (int t = 0; t < klen; t++) {
            int diff = keys[t], cnt = dp[diff + OFF2143];
            ADD(diff + nums1[i], cnt);
            ADD(diff - nums2[i], cnt);
        }
        int* tmp = dp; dp = ndp; ndp = tmp;
        int* tk = keys; keys = nkeys; nkeys = tk;
        klen = nlen;
        ans = (ans + dp[0 + OFF2143]) % MOD2143;
    }
    free(dp); free(ndp); free(keys); free(nkeys);
    return ans;
}
