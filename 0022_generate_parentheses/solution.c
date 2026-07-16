// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

#include <stdlib.h>
#include <string.h>

static void backtrack(
    char* path,
    int pathLen,
    int n,
    int openCount,
    int closeCount,
    char*** result,
    int* count,
    int* capacity
) {
    if (pathLen == 2 * n) {
        if (*count >= *capacity) {
            *capacity *= 2;
            *result = (char**)realloc(*result, (size_t)(*capacity) * sizeof(char*));
        }
        (*result)[*count] = (char*)malloc((size_t)pathLen + 1);
        memcpy((*result)[*count], path, (size_t)pathLen + 1);
        (*count)++;
        return;
    }
    if (openCount < n) {
        path[pathLen] = '(';
        path[pathLen + 1] = '\0';
        backtrack(path, pathLen + 1, n, openCount + 1, closeCount, result, count, capacity);
    }
    if (closeCount < openCount) {
        path[pathLen] = ')';
        path[pathLen + 1] = '\0';
        backtrack(path, pathLen + 1, n, openCount, closeCount + 1, result, count, capacity);
    }
}

char** generateParenthesis(int n, int* returnSize) {
    int capacity = 16;
    char** result = (char**)malloc((size_t)capacity * sizeof(char*));
    char path[32] = {0};
    *returnSize = 0;
    backtrack(path, 0, n, 0, 0, &result, returnSize, &capacity);
    result = (char**)realloc(result, (size_t)(*returnSize) * sizeof(char*));
    return result;
}
