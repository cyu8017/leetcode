// LeetCode 0320 - Generalized Abbreviation
// https://leetcode.com/problems/generalized-abbreviation/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void pushResult(char*** result, int* resultSize, int* resultCapacity, const char* value) {
    if (*resultSize == *resultCapacity) {
        *resultCapacity = *resultCapacity ? *resultCapacity * 2 : 16;
        *result = (char**)realloc(*result, (size_t)(*resultCapacity) * sizeof(char*));
    }
    (*result)[*resultSize] = strdup(value);
    (*resultSize)++;
}

static void backtrack(
    const char* word,
    int index,
    const char* path,
    int count,
    char*** result,
    int* resultSize,
    int* resultCapacity
) {
    if (word[index] == '\0') {
        char final[128];
        if (count > 0) {
            snprintf(final, sizeof(final), "%s%d", path, count);
        } else {
            strncpy(final, path, sizeof(final) - 1);
            final[sizeof(final) - 1] = '\0';
        }
        pushResult(result, resultSize, resultCapacity, final);
        return;
    }

    backtrack(word, index + 1, path, count + 1, result, resultSize, resultCapacity);

    char nextPath[128];
    if (count > 0) {
        snprintf(nextPath, sizeof(nextPath), "%s%d%c", path, count, word[index]);
    } else {
        snprintf(nextPath, sizeof(nextPath), "%s%c", path, word[index]);
    }
    backtrack(word, index + 1, nextPath, 0, result, resultSize, resultCapacity);
}

char** generateAbbreviations(char* word, int* returnSize) {
    int resultCapacity = 16;
    char** result = (char**)malloc((size_t)resultCapacity * sizeof(char*));
    *returnSize = 0;
    backtrack(word, 0, "", 0, &result, returnSize, &resultCapacity);
    result = (char**)realloc(result, (size_t)(*returnSize) * sizeof(char*));
    return result;
}
