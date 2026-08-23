// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

#include <stdlib.h>
#include <limits.h>

static int gcd4005(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

static int cost4005(int x, int t) {
    if (x == t) return 0;
    if (x % t == 0 || t % x == 0) return 1;
    return 2;
}

static int cmpInt4005(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int minOperations(int* nums, int numsSize) {
    if (numsSize <= 1) return 0;

    int g = nums[0], mn = nums[0];
    for (int i = 1; i < numsSize; i++) {
        g = gcd4005(g, nums[i]);
        if (nums[i] < mn) mn = nums[i];
    }

    int cap = numsSize * 2 + 128;
    int* cands = (int*)malloc((size_t)cap * sizeof(int));
    int cn = 0;

    /* unique values */
    int* tmp = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) tmp[i] = nums[i];
    qsort(tmp, (size_t)numsSize, sizeof(int), cmpInt4005);
    for (int i = 0; i < numsSize; i++) {
        if (i == 0 || tmp[i] != tmp[i - 1]) {
            if (cn == cap) {
                cap *= 2;
                cands = (int*)realloc(cands, (size_t)cap * sizeof(int));
            }
            cands[cn++] = tmp[i];
        }
    }
    free(tmp);

    /* divisors of minimum */
    for (int d = 1; (long long)d * d <= mn; d++) {
        if (mn % d == 0) {
            if (cn + 2 >= cap) {
                cap = cn + 64;
                cands = (int*)realloc(cands, (size_t)cap * sizeof(int));
            }
            int found = 0;
            for (int i = 0; i < cn; i++) if (cands[i] == d) { found = 1; break; }
            if (!found) cands[cn++] = d;
            int d2 = mn / d;
            found = 0;
            for (int i = 0; i < cn; i++) if (cands[i] == d2) { found = 1; break; }
            if (!found) {
                if (cn == cap) {
                    cap *= 2;
                    cands = (int*)realloc(cands, (size_t)cap * sizeof(int));
                }
                cands[cn++] = d2;
            }
        }
    }

    /* gcd of all */
    {
        int found = 0;
        for (int i = 0; i < cn; i++) if (cands[i] == g) { found = 1; break; }
        if (!found) {
            if (cn == cap) {
                cap *= 2;
                cands = (int*)realloc(cands, (size_t)cap * sizeof(int));
            }
            cands[cn++] = g;
        }
    }

    int ans = INT_MAX;
    for (int ci = 0; ci < cn; ci++) {
        int t = cands[ci];
        int sum = 0;
        for (int i = 0; i < numsSize; i++) {
            sum += cost4005(nums[i], t);
            if (sum >= ans) break;
        }
        if (sum < ans) ans = sum;
    }
    free(cands);
    return ans;
}
