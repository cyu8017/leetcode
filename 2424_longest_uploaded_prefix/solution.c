// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    bool* uploaded;
    int longest;
    int n;
} LUPrefix;

LUPrefix* lUPrefixCreate(int n) {
    LUPrefix* obj = (LUPrefix*)calloc(1, sizeof(LUPrefix));
    obj->n = n;
    obj->uploaded = (bool*)calloc((size_t)(n + 2), sizeof(bool));
    return obj;
}

void lUPrefixUpload(LUPrefix* obj, int video) {
    obj->uploaded[video] = true;
    while (obj->uploaded[obj->longest + 1]) obj->longest++;
}

int lUPrefixLongest(LUPrefix* obj) {
    return obj->longest;
}

void lUPrefixFree(LUPrefix* obj) {
    if (!obj) return;
    free(obj->uploaded);
    free(obj);
}
