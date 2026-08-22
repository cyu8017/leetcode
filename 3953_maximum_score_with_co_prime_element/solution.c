// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int* divisible3953;

static int badCount3953(int x) {
    int primes[16], pn = 0;
    int y = x;
    for (int p = 2; p * p <= y; p++) {
        if (y % p == 0) {
            primes[pn++] = p;
            while (y % p == 0) y /= p;
        }
    }
    if (y > 1) primes[pn++] = y;
    int bad = 0;
    for (int mask = 1; mask < (1 << pn); mask++) {
        int product = 1, bits = 0;
        for (int i = 0; i < pn; i++) if ((mask >> i) & 1) { product *= primes[i]; bits++; }
        if (bits % 2 == 1) bad += divisible3953[product];
        else bad -= divisible3953[product];
    }
    return bad;
}

int maxScore(int* nums, int numsSize, int maxVal) {
    int frequency[100001];
    memset(frequency, 0, sizeof(frequency));
    int limit = maxVal;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < 100001) frequency[nums[i]]++;
        if (nums[i] > limit) limit = nums[i];
    }
    divisible3953 = calloc((size_t)(limit + 1), sizeof(int));
    for (int d = 1; d <= limit; d++) {
        for (int multiple = d; multiple <= limit; multiple += d) {
            if (multiple < 100001) divisible3953[d] += frequency[multiple];
        }
    }
    int best = -numsSize;
    bool* checked = calloc((size_t)(limit + 1), 1);
    for (int x = 1; x <= maxVal; x++) {
        if (checked[x]) continue;
        checked[x] = true;
        int exists = x < 100001 && frequency[x] > 0;
        int bad = badCount3953(x);
        int cost = 0;
        if (exists) { if (x > 1) cost = bad - 1; }
        else if (bad > 0) cost = bad;
        else cost = 1;
        if (x - cost > best) best = x - cost;
    }
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x < 0 || x > limit || checked[x]) continue;
        checked[x] = true;
        int bad = badCount3953(x);
        int cost = (x > 1) ? bad - 1 : 0;
        if (x - cost > best) best = x - cost;
    }
    free(divisible3953); free(checked);
    return best;
}
