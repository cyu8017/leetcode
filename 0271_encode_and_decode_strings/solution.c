// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* encode(char** strs, int strsSize) {
    size_t total = 1;
    for (int i = 0; i < strsSize; i++) {
        total += 16 + strlen(strs[i]);
    }

    char* encoded = (char*)malloc(total);
    if (!encoded) {
        return NULL;
    }
    encoded[0] = '\0';

    for (int i = 0; i < strsSize; i++) {
        char buffer[64];
        snprintf(buffer, sizeof(buffer), "%zu#%s", strlen(strs[i]), strs[i]);
        strcat(encoded, buffer);
    }
    return encoded;
}

/**
 * Return an array of size *returnSize.
 */
char** decode(char* encoded, int* returnSize) {
    *returnSize = 0;
    if (!encoded || encoded[0] == '\0') {
        return NULL;
    }

    int count = 0;
    for (char* cursor = encoded; *cursor; cursor++) {
        if (*cursor == '#') {
            count++;
        }
    }

    char** result = (char**)malloc((size_t)count * sizeof(char*));
    if (!result) {
        return NULL;
    }

    int index = 0;
    int out = 0;
    size_t length = strlen(encoded);
    while ((size_t)index < length) {
        int delimiter = index;
        while ((size_t)delimiter < length && encoded[delimiter] != '#') {
            delimiter++;
        }
        int chunk = atoi(encoded + index);
        int start = delimiter + 1;
        result[out] = (char*)malloc((size_t)chunk + 1);
        memcpy(result[out], encoded + start, (size_t)chunk);
        result[out][chunk] = '\0';
        index = start + chunk;
        out++;
    }
    *returnSize = out;
    return result;
}
