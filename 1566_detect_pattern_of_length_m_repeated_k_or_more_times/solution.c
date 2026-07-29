// LeetCode 1566 - Detect Pattern of Length M Repeated K or More Times
// https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/

#include <stdbool.h>

bool containsPattern(int* arr, int arrSize, int m, int k) {
    int run = 0;
    for (int i = m; i < arrSize; i++) {
        run = (arr[i] == arr[i - m]) ? run + 1 : 0;
        if (run >= m * (k - 1)) return true;
    }
    return false;
}
