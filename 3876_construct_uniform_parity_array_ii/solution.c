// LeetCode 3876 - Construct Uniform Parity Array Ii
// https://leetcode.com/problems/construct-uniform-parity-array-ii/

#include <stdbool.h>
#include <limits.h>

bool uniformArray(int* nums1, int nums1Size) {
    int mn = INT_MAX;
    for (int i = 0; i < nums1Size; i++) {
        int x = nums1[i];
        if (x % 2 == 1 && x < mn) mn = x;
    }
    for (int i = 0; i < nums1Size; i++) {
        int x = nums1[i];
        if (x % 2 == 0 && mn != INT_MAX && x < mn) return false;
    }
    return true;
}
