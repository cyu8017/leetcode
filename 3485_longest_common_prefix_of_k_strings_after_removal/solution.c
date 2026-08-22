// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

#include <stdlib.h>
#include <string.h>

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

static int lcpOf(char** a, int k) {
    if (k == 0) return 0;
    int plen = (int)strlen(a[0]);
    for (int t = 1; t < k; t++) {
        int i = 0;
        int sl = (int)strlen(a[t]);
        while (i < plen && i < sl && a[0][i] == a[t][i]) i++;
        plen = i;
        if (plen == 0) return 0;
    }
    /* recompute vs all after mutating conceptually - use first and last of sorted window */
    char* first = a[0];
    char* last = a[k - 1];
    int i = 0;
    while (first[i] && last[i] && first[i] == last[i]) i++;
    return i;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestCommonPrefix(char** words, int wordsSize, int k, int* returnSize) {
    int n = wordsSize;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        char** rest = (char**)malloc((size_t)(n - 1) * sizeof(char*));
        int rc = 0;
        for (int j = 0; j < n; j++) {
            if (j != i) rest[rc++] = words[j];
        }
        if (rc < k) {
            ans[i] = 0;
            free(rest);
            continue;
        }
        qsort(rest, (size_t)rc, sizeof(char*), cmp_str);
        int best = 0;
        for (int j = 0; j + k - 1 < rc; j++) {
            int lcp = lcpOf(rest + j, k);
            if (lcp > best) best = lcp;
        }
        ans[i] = best;
        free(rest);
    }
    *returnSize = n;
    return ans;
}
