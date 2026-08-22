// LeetCode 3739 - Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

#include <stdlib.h>

typedef struct { int n; int* c; } BIT;

static BIT* newBIT(int n) {
    BIT* t = (BIT*)malloc(sizeof(BIT));
    t->n = n;
    t->c = (int*)calloc((size_t)(n + 1), sizeof(int));
    return t;
}
static void bitUpdate(BIT* t, int x, int delta) {
    for (; x <= t->n; x += x & -x) t->c[x] += delta;
}
static int bitQuery(BIT* t, int x) {
    int s = 0;
    for (; x > 0; x -= x & -x) s += t->c[x];
    return s;
}

long long countMajoritySubarrays(int* nums, int numsSize, int target) {
    int n = numsSize;
    BIT* tree = newBIT(2 * n + 1);
    int s = n + 1;
    bitUpdate(tree, s, 1);
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == target) s++; else s--;
        ans += bitQuery(tree, s - 1);
        bitUpdate(tree, s, 1);
    }
    free(tree->c); free(tree);
    return ans;
}
