// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

#include <stdlib.h>
static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }
static int imax(int a,int b){return a>b?a:b;}
int minRemoval(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    int n = numsSize, cnt = 0;
    for (int i = 0; i < n; i++) {
        int j = n;
        if ((long long)nums[i] * k <= nums[n - 1]) {
            long long target = (long long)nums[i] * k + 1;
            int lo = 0, hi = n;
            while (lo < hi) { int mid = (lo + hi) / 2; if (nums[mid] >= target) hi = mid; else lo = mid + 1; }
            j = lo;
        }
        cnt = imax(cnt, j - i);
    }
    return n - cnt;
}
