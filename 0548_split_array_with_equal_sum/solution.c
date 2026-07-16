// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

#include <stdbool.h>
#include <stdlib.h>

static bool contains_value(long long* values, int size, long long target) {
    for (int index = 0; index < size; index++) {
        if (values[index] == target) {
            return true;
        }
    }
    return false;
}

static void add_value(long long** values, int* size, int* capacity, long long target) {
    if (contains_value(*values, *size, target)) {
        return;
    }
    if (*size >= *capacity) {
        *capacity = (*capacity == 0) ? 16 : (*capacity * 2);
        *values = (long long*)realloc(*values, (size_t)(*capacity) * sizeof(long long));
    }
    (*values)[(*size)++] = target;
}

bool splitArray(int* nums, int numsSize) {
    const int n = numsSize;
    if (n < 7) {
        return false;
    }

    long long* prefix = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int index = 0; index < n; index++) {
        prefix[index + 1] = prefix[index] + nums[index];
    }

    for (int j = 3; j < n - 3; j++) {
        long long* seen = NULL;
        int seenSize = 0;
        int seenCapacity = 0;

        for (int i = 1; i < j - 1; i++) {
            const long long first = prefix[i] - prefix[0];
            const long long second = prefix[j] - prefix[i + 1];
            if (first == second) {
                add_value(&seen, &seenSize, &seenCapacity, first);
            }
        }

        for (int k = j + 2; k < n - 1; k++) {
            const long long third = prefix[k] - prefix[j + 1];
            const long long fourth = prefix[n] - prefix[k + 1];
            if (third == fourth && contains_value(seen, seenSize, third)) {
                free(seen);
                free(prefix);
                return true;
            }
        }

        free(seen);
    }

    free(prefix);
    return false;
}
