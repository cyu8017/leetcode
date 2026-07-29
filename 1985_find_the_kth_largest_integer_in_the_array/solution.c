// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

#include <stdlib.h>
#include <string.h>

static int cmpNumStrDesc(const void* a, const void* b) {
    const char* x = *(const char* const*)a;
    const char* y = *(const char* const*)b;
    size_t lx = strlen(x), ly = strlen(y);
    if (lx != ly) return lx > ly ? -1 : 1;
    int c = strcmp(x, y);
    return -c;
}

char* kthLargestNumber(char** nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(char*), cmpNumStrDesc);
    char* res = (char*)malloc(strlen(nums[k - 1]) + 1);
    strcpy(res, nums[k - 1]);
    return res;
}
