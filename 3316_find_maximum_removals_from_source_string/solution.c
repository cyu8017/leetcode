// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool ok3316(int removeFirst, char* source, char* pattern, int* targetIndices, int n) {
    bool* mark = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < removeFirst; i++) mark[targetIndices[i]] = true;
    int j = 0, m = (int)strlen(pattern);
    for (int i = 0; i < n && j < m; i++) {
        if (mark[i]) continue;
        if (source[i] == pattern[j]) j++;
    }
    free(mark);
    return j == m;
}

int maxRemovals(char* source, char* pattern, int* targetIndices, int targetIndicesSize) {
    int n = (int)strlen(source);
    int lo = 0, hi = targetIndicesSize;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (ok3316(mid, source, pattern, targetIndices, n)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
