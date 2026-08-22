// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

#include <stdlib.h>

int valueAfterKSeconds(int n, int k) {
    const int mod = 1000000007;
    int* a = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) a[i] = 1;
    while (k-- > 0)
        for (int i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
    int ans = a[n - 1];
    free(a);
    return ans;
}
