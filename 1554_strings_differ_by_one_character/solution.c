// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool differByOne(char** dict, int dictSize) {
    if (dictSize == 0) return false;
    int len = (int)strlen(dict[0]);
    int cap = 1;
    while (cap < dictSize * len * 2 + 8) cap <<= 1;
    char** keys = (char**)calloc((size_t)cap, sizeof(char*));
    for (int w = 0; w < dictSize; w++) {
        char* word = dict[w];
        for (int i = 0; i < len; i++) {
            char* pattern = (char*)malloc((size_t)len + 1);
            memcpy(pattern, word, (size_t)len);
            pattern[len] = '\0';
            pattern[i] = '*';
            unsigned h = 2166136261u;
            for (int k = 0; k < len; k++) {
                h ^= (unsigned char)pattern[k];
                h *= 16777619u;
            }
            h %= (unsigned)cap;
            while (keys[h]) {
                if (strcmp(keys[h], pattern) == 0) {
                    free(pattern);
                    for (int t = 0; t < cap; t++) free(keys[t]);
                    free(keys);
                    return true;
                }
                h = (h + 1) % (unsigned)cap;
            }
            keys[h] = pattern;
        }
    }
    for (int t = 0; t < cap; t++) free(keys[t]);
    free(keys);
    return false;
}
