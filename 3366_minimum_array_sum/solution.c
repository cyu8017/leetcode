// LeetCode 3366 - Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/

#include <stdlib.h>
#include <string.h>

int minArraySum(int* nums, int numsSize, int k, int op1, int op2) {
    const long long INF = 1000000000000000000LL;
    long long* dp = (long long*)malloc((op1 + 1) * (op2 + 1) * sizeof(long long));
    long long* ndp = (long long*)malloc((op1 + 1) * (op2 + 1) * sizeof(long long));
    #define AT(p,a,b) ((p)[(a)*(op2+1)+(b)])
    for (int i = 0; i <= op1; i++) for (int j = 0; j <= op2; j++) AT(dp, i, j) = INF;
    AT(dp, 0, 0) = 0;
    for (int idx = 0; idx < numsSize; idx++) {
        int x = nums[idx];
        for (int i = 0; i <= op1; i++) for (int j = 0; j <= op2; j++) AT(ndp, i, j) = INF;
        for (int a = 0; a <= op1; a++) for (int b = 0; b <= op2; b++) {
            if (AT(dp, a, b) == INF) continue;
            long long base = AT(dp, a, b);
            if (base + x < AT(ndp, a, b)) AT(ndp, a, b) = base + x;
            if (a < op1) {
                long long v = (x + 1) / 2;
                if (base + v < AT(ndp, a + 1, b)) AT(ndp, a + 1, b) = base + v;
            }
            if (b < op2 && x >= k) {
                long long v = x - k;
                if (base + v < AT(ndp, a, b + 1)) AT(ndp, a, b + 1) = base + v;
            }
            if (a < op1 && b < op2) {
                long long v1 = (x + 1) / 2;
                if (v1 >= k && base + v1 - k < AT(ndp, a + 1, b + 1)) AT(ndp, a + 1, b + 1) = base + v1 - k;
                if (x >= k) {
                    long long v2 = (x - k + 1) / 2;
                    if (base + v2 < AT(ndp, a + 1, b + 1)) AT(ndp, a + 1, b + 1) = base + v2;
                }
            }
        }
        long long* tmp = dp; dp = ndp; ndp = tmp;
    }
    long long ans = INF;
    for (int a = 0; a <= op1; a++) for (int b = 0; b <= op2; b++) if (AT(dp, a, b) < ans) ans = AT(dp, a, b);
    free(dp); free(ndp);
    return (int)ans;
}
