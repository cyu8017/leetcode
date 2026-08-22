// LeetCode 0553 - Optimal Division
// https://leetcode.com/problems/optimal-division/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* optimalDivision(int* nums, int numsSize) {
    char* result = (char*)malloc(256);
    if (numsSize == 1) {
        sprintf(result, "%d", nums[0]);
        return result;
    }
    if (numsSize == 2) {
        sprintf(result, "%d/%d", nums[0], nums[1]);
        return result;
    }

    int pos = sprintf(result, "%d/(", nums[0]);
    for (int i = 1; i < numsSize; i++) {
        if (i > 1) {
            result[pos++] = '/';
        }
        pos += sprintf(result + pos, "%d", nums[i]);
    }
    result[pos++] = ')';
    result[pos] = '\0';
    return result;
}
