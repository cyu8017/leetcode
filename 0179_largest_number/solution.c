// LeetCode 0179 - Largest Number
// https://leetcode.com/problems/largest-number/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int compare(const void* left, const void* right) {
    const char* a = *(const char* const*)left;
    const char* b = *(const char* const*)right;
    char ab[22];
    char ba[22];
    snprintf(ab, sizeof(ab), "%s%s", a, b);
    snprintf(ba, sizeof(ba), "%s%s", b, a);
    return strcmp(ba, ab);
}

char* largestNumber(int* nums, int numsSize) {
    char** parts = malloc(numsSize * sizeof(*parts));
    size_t totalLength = 0;
    for (int i = 0; i < numsSize; i++) {
        parts[i] = malloc(11);
        snprintf(parts[i], 11, "%d", nums[i]);
        totalLength += strlen(parts[i]);
    }
    qsort(parts, numsSize, sizeof(*parts), compare);

    if (parts[0][0] == '0') {
        for (int i = 0; i < numsSize; i++) {
            free(parts[i]);
        }
        free(parts);
        char* result = malloc(2);
        strcpy(result, "0");
        return result;
    }

    char* result = malloc(totalLength + 1);
    result[0] = '\0';
    for (int i = 0; i < numsSize; i++) {
        strcat(result, parts[i]);
        free(parts[i]);
    }
    free(parts);
    return result;
}