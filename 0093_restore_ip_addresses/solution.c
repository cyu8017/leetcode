// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void backtrack(
    char* s,
    int start,
    int n,
    char parts[4][4],
    int partCount,
    char*** result,
    int* count,
    int* capacity
) {
    if (partCount == 4) {
        if (start == n) {
            if (*count >= *capacity) {
                *capacity *= 2;
                *result = (char**)realloc(*result, (size_t)(*capacity) * sizeof(char*));
            }
            (*result)[*count] = (char*)malloc(16);
            sprintf((*result)[*count], "%s.%s.%s.%s", parts[0], parts[1], parts[2], parts[3]);
            (*count)++;
        }
        return;
    }

    for (int length = 1; length <= 3; length++) {
        if (start + length > n) {
            break;
        }
        if (s[start] == '0' && length > 1) {
            continue;
        }
        int value = 0;
        for (int i = 0; i < length; i++) {
            value = value * 10 + (s[start + i] - '0');
        }
        if (value > 255) {
            continue;
        }
        memcpy(parts[partCount], s + start, (size_t)length);
        parts[partCount][length] = '\0';
        backtrack(s, start + length, n, parts, partCount + 1, result, count, capacity);
    }
}

char** restoreIpAddresses(char* s, int* returnSize) {
    int capacity = 8;
    char** result = (char**)malloc((size_t)capacity * sizeof(char*));
    char parts[4][4];
    *returnSize = 0;
    backtrack(s, 0, (int)strlen(s), parts, 0, &result, returnSize, &capacity);
    result = (char**)realloc(result, (size_t)(*returnSize) * sizeof(char*));
    return result;
}
