// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

static int findp(int* p, int x) {
    while (p[x] != x) { p[x] = p[p[x]]; x = p[x]; }
    return x;
}

static bool similar(const char* a, const char* b) {
    int d0 = -1, d1 = -1, diffs = 0;
    for (int i = 0; a[i]; i++) {
        if (a[i] != b[i]) {
            if (diffs == 0) d0 = i;
            else if (diffs == 1) d1 = i;
            else return false;
            diffs++;
        }
    }
    if (diffs == 0) return true;
    if (diffs != 2) return false;
    return a[d0] == b[d1] && a[d1] == b[d0];
}

int numSimilarGroups(char** strs, int strsSize) {
    int* parent = (int*)malloc((size_t)strsSize * sizeof(int));
    for (int i = 0; i < strsSize; i++) parent[i] = i;
    int groups = strsSize;
    for (int i = 0; i < strsSize; i++) {
        for (int j = i + 1; j < strsSize; j++) {
            if (similar(strs[i], strs[j])) {
                int pi = findp(parent, i), pj = findp(parent, j);
                if (pi != pj) { parent[pi] = pj; groups--; }
            }
        }
    }
    free(parent);
    return groups;
}
