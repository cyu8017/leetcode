// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int largestInteger(int num) {
    int digits[16], n = 0;
    int x = num;
    if (x == 0) digits[n++] = 0;
    else {
        int tmp[16], m = 0;
        while (x > 0) { tmp[m++] = x % 10; x /= 10; }
        for (int i = m - 1; i >= 0; i--) digits[n++] = tmp[i];
    }
    int even[16], odd[16], ec = 0, oc = 0;
    for (int i = 0; i < n; i++) {
        if (digits[i] % 2 == 0) even[ec++] = digits[i];
        else odd[oc++] = digits[i];
    }
    qsort(even, (size_t)ec, sizeof(int), cmp_desc);
    qsort(odd, (size_t)oc, sizeof(int), cmp_desc);
    int ei = 0, oi = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        if (digits[i] % 2 == 0) ans = ans * 10 + even[ei++];
        else ans = ans * 10 + odd[oi++];
    }
    return ans;
}
