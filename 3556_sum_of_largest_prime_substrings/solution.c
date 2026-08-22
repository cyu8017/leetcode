// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

#include <math.h>
#include <stdlib.h>
#include <string.h>

static int isPrime(long long x) {
    if (x < 2) return 0;
    long long sq = (long long)sqrt((double)x);
    for (long long i = 2; i <= sq; i++) if (x % i == 0) return 0;
    return 1;
}

static int cmp_ll(const void* a, const void* b) {
    long long x = *(const long long*)a, y = *(const long long*)b;
    return (x > y) - (x < y);
}

long long sumOfLargestPrimes(char* s) {
    int n = (int)strlen(s);
    long long* nums = (long long*)malloc((size_t)(n * n + 1) * sizeof(long long));
    int nc = 0;
    for (int i = 0; i < n; i++) {
        long long x = 0;
        for (int j = i; j < n; j++) {
            x = x * 10 + (s[j] - '0');
            if (isPrime(x)) {
                int dup = 0;
                for (int t = 0; t < nc; t++) if (nums[t] == x) { dup = 1; break; }
                if (!dup) nums[nc++] = x;
            }
        }
    }
    qsort(nums, (size_t)nc, sizeof(long long), cmp_ll);
    long long ans = 0;
    int taken = 0;
    for (int i = nc - 1; i >= 0 && taken < 3; i--, taken++) ans += nums[i];
    free(nums);
    return ans;
}
