// LeetCode 3024 - Type of Triangle
// https://leetcode.com/problems/type-of-triangle/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

char* triangleType(int* nums, int numsSize) {
    (void)numsSize;
    int a[3] = {nums[0], nums[1], nums[2]};
    qsort(a, 3, sizeof(int), cmp_int);
    if (a[0] + a[1] <= a[2]) return "none";
    if (a[0] == a[2]) return "equilateral";
    if (a[0] == a[1] || a[1] == a[2]) return "isosceles";
    return "scalene";
}
