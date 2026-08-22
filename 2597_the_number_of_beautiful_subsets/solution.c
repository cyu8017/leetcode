// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int beautifulSubsets(int* nums, int numsSize, int k) {
    int freq[1001];
    memset(freq, 0, sizeof(freq));
    for (int i = 0; i < numsSize; i++) freq[nums[i]]++;
    int ans = 1;
    for (int rem = 0; rem < k; rem++) {
        int vals[1001], vc = 0;
        for (int v = 1; v <= 1000; v++) {
            if (freq[v] && v % k == rem) vals[vc++] = v;
        }
        if (vc == 0) continue;
        qsort(vals, (size_t)vc, sizeof(int), cmpInt);
        int prevTake = 0, prevSkip = 1, prevVal = -1000000000;
        for (int i = 0; i < vc; i++) {
            int v = vals[i];
            int ways = 1;
            for (int j = 0; j < freq[v]; j++) ways *= 2;
            ways--;
            int skip = prevTake + prevSkip;
            int take = ways * prevSkip;
            if (prevVal + k != v) take += ways * prevTake;
            prevTake = take;
            prevSkip = skip;
            prevVal = v;
        }
        ans *= prevTake + prevSkip;
    }
    return ans - 1;
}
