// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

static bool matches(char* q, char* pattern) {
    int i = 0;
    for (char* p = q; *p; p++) {
        if (pattern[i] && *p == pattern[i]) i++;
        else if (isupper((unsigned char)*p)) return false;
    }
    return pattern[i] == '\0';
}

bool* camelMatch(char** queries, int queriesSize, char* pattern, int* returnSize) {
    bool* ans = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    *returnSize = queriesSize;
    for (int i = 0; i < queriesSize; i++)
        ans[i] = matches(queries[i], pattern);
    return ans;
}
