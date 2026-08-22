// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

#include <stdlib.h>
#include <string.h>

enum { H3134 = 200003 };

typedef struct { int key, val, used; } E3134;

static int ok3134(int* nums, int n, int mx, long long need) {
    E3134* ht = calloc(H3134, sizeof(E3134));
    int distinct = 0, l = 0;
    long long k = 0;
    for (int r = 0; r < n; r++) {
        unsigned h = ((unsigned)nums[r] * 2654435761u) % H3134;
        while (ht[h].used && ht[h].key != nums[r]) h = (h + 1) % H3134;
        if (!ht[h].used) { ht[h].used = 1; ht[h].key = nums[r]; ht[h].val = 0; distinct++; }
        ht[h].val++;
        while (distinct > mx) {
            unsigned h2 = ((unsigned)nums[l] * 2654435761u) % H3134;
            while (ht[h2].key != nums[l]) h2 = (h2 + 1) % H3134;
            ht[h2].val--;
            if (ht[h2].val == 0) { ht[h2].used = 0; distinct--; }
            l++;
        }
        k += r - l + 1;
        if (k >= need) { free(ht); return 1; }
    }
    free(ht);
    return 0;
}

int medianOfUniquenessArray(int* nums, int numsSize) {
    long long m = (1LL + numsSize) * numsSize / 2;
    long long need = (m + 1) / 2;
    int lo = 1, hi = numsSize;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (ok3134(nums, numsSize, mid, need)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
