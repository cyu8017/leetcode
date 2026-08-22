// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

#include <stdbool.h>

static int popcount(unsigned x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}

bool canSortArray(int* nums, int numsSize) {
    int preMx = 0, i = 0;
    while (i < numsSize) {
        int cnt = popcount((unsigned)nums[i]);
        int j = i + 1, mi = nums[i], mx = nums[i];
        while (j < numsSize && popcount((unsigned)nums[j]) == cnt) {
            if (nums[j] < mi) mi = nums[j];
            if (nums[j] > mx) mx = nums[j];
            j++;
        }
        if (preMx > mi) return false;
        preMx = mx;
        i = j;
    }
    return true;
}
