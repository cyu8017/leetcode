// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

#include <stdbool.h>

static int gcd_int(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a < 0 ? -a : a;
}

bool isGoodArray(int* nums, int numsSize) {
    int g = 0;
    for (int i = 0; i < numsSize; i++) g = gcd_int(g, nums[i]);
    return g == 1;
}
