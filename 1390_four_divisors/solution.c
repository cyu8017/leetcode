// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

#include <math.h>

int sumFourDivisors(int* nums, int numsSize) {
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int ds[16], dn = 0;
        int lim = (int)sqrt((double)x);
        for (int d = 1; d <= lim; d++) {
            if (x % d == 0) {
                ds[dn++] = d;
                if (d != x / d) ds[dn++] = x / d;
                if (dn > 4) break;
            }
        }
        if (dn == 4) {
            int s = 0;
            for (int j = 0; j < 4; j++) s += ds[j];
            ans += s;
        }
    }
    return ans;
}
