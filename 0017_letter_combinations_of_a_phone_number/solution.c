// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#include <stdlib.h>
#include <string.h>

static const char* MAPPING[10] = {
    "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
};

static void backtrack(
    char* digits,
    int index,
    char* path,
    int pathLen,
    char*** result,
    int* count,
    int* capacity
) {
    if (digits[index] == '\0') {
        if (*count >= *capacity) {
            *capacity *= 2;
            *result = (char**)realloc(*result, (size_t)(*capacity) * sizeof(char*));
        }
        (*result)[*count] = (char*)malloc((size_t)pathLen + 1);
        memcpy((*result)[*count], path, (size_t)pathLen + 1);
        (*count)++;
        return;
    }

    const char* letters = MAPPING[digits[index] - '0'];
    for (int i = 0; letters[i] != '\0'; i++) {
        path[pathLen] = letters[i];
        path[pathLen + 1] = '\0';
        backtrack(digits, index + 1, path, pathLen + 1, result, count, capacity);
    }
}

char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    if (digits == NULL || digits[0] == '\0') {
        return NULL;
    }

    int capacity = 8;
    char** result = (char**)malloc((size_t)capacity * sizeof(char*));
    char path[16] = {0};
    backtrack(digits, 0, path, 0, &result, returnSize, &capacity);
    result = (char**)realloc(result, (size_t)(*returnSize) * sizeof(char*));
    return result;
}
