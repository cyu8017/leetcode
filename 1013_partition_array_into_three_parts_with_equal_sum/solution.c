// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

#include <stdbool.h>

bool canThreePartsEqualSum(int* arr, int arrSize) {
    int total = 0;
    for (int i = 0; i < arrSize; i++) total += arr[i];
    if (total % 3 != 0) return false;
    int target = total / 3, parts = 0, cur = 0;
    for (int i = 0; i < arrSize; i++) {
        cur += arr[i];
        if (cur == target) {
            parts++;
            cur = 0;
        }
    }
    return parts >= 3;
}
