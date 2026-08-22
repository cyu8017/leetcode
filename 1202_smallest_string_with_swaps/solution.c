// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

#include <stdlib.h>
#include <string.h>

static int find(int* parent, int x) {
    while (x != parent[x]) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

static int cmpCharDesc(const void* a, const void* b) {
    return *(const char*)b - *(const char*)a;
}

char* smallestStringWithSwaps(char* s, int** pairs, int pairsSize, int* pairsColSize) {
    (void)pairsColSize;
    int n = (int)strlen(s);
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < pairsSize; i++) {
        int ra = find(parent, pairs[i][0]);
        int rb = find(parent, pairs[i][1]);
        parent[ra] = rb;
    }
    char** groups = (char**)calloc((size_t)n, sizeof(char*));
    int* sizes = (int*)calloc((size_t)n, sizeof(int));
    int* caps = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        int root = find(parent, i);
        if (sizes[root] >= caps[root]) {
            caps[root] = caps[root] ? caps[root] * 2 : 4;
            groups[root] = (char*)realloc(groups[root], (size_t)caps[root]);
        }
        groups[root][sizes[root]++] = s[i];
    }
    for (int i = 0; i < n; i++) {
        if (groups[i]) qsort(groups[i], (size_t)sizes[i], 1, cmpCharDesc);
    }
    char* ans = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        int root = find(parent, i);
        ans[i] = groups[root][--sizes[root]];
    }
    ans[n] = '\0';
    for (int i = 0; i < n; i++) free(groups[i]);
    free(groups);
    free(sizes);
    free(caps);
    free(parent);
    return ans;
}
