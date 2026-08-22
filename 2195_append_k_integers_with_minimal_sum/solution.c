// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long minimalKSum(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmpAsc);
    long long ans = 0;
    int prev = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x <= prev) continue;
        int start = prev + 1, end = x - 1;
        if (start <= end) {
            int cnt = end - start + 1;
            if (cnt > k) { end = start + k - 1; cnt = k; }
            ans += (long long)(start + end) * cnt / 2;
            k -= cnt;
            if (k == 0) return ans;
        }
        prev = x;
    }
    int start = prev + 1, end = start + k - 1;
    ans += (long long)(start + end) * k / 2;
    return ans;
}
