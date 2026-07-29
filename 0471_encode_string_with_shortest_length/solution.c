// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

#define _POSIX_C_SOURCE 200809L

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int isBetter(const char* a, const char* b) {
    int la = (int)strlen(a);
    int lb = (int)strlen(b);
    if (la != lb) {
        return la < lb;
    }
    return strcmp(a, b) < 0;
}

static char* encodeWord(const char* word, int size) {
    char* best = (char*)malloc((size_t)size + 1);
    memcpy(best, word, (size_t)size);
    best[size] = '\0';

    for (int unitLength = 1; unitLength <= size / 2; unitLength++) {
        if (size % unitLength != 0) {
            continue;
        }
        int ok = 1;
        for (int i = unitLength; i < size; i++) {
            if (word[i] != word[i % unitLength]) {
                ok = 0;
                break;
            }
        }
        if (!ok) {
            continue;
        }
        char* encoded = (char*)malloc(64 + (size_t)unitLength);
        sprintf(encoded, "%d[", size / unitLength);
        strncat(encoded, word, (size_t)unitLength);
        strcat(encoded, "]");
        if (isBetter(encoded, best)) {
            free(best);
            best = encoded;
        } else {
            free(encoded);
        }
    }
    return best;
}

char* encode(char* s) {
    int length = (int)strlen(s);
    char** dp = (char**)calloc((size_t)length + 1, sizeof(char*));
    dp[0] = strdup("");

    for (int index = 1; index <= length; index++) {
        dp[index] = encodeWord(s, index);
        for (int split = 1; split < index; split++) {
            char* part = encodeWord(s + index - split, split);
            char* candidate = (char*)malloc(strlen(dp[index - split]) + strlen(part) + 1);
            strcpy(candidate, dp[index - split]);
            strcat(candidate, part);
            free(part);
            if (isBetter(candidate, dp[index])) {
                free(dp[index]);
                dp[index] = candidate;
            } else {
                free(candidate);
            }
        }
    }

    char* result = dp[length];
    for (int i = 0; i < length; i++) {
        free(dp[i]);
    }
    free(dp);
    return result;
}
