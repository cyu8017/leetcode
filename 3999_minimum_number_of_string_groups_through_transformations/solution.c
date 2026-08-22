// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

#include <stdlib.h>
#include <string.h>

static int leastRotation(const char* s, int n) {
    int i = 0, j = 1, k = 0;
    while (i < n && j < n && k < n) {
        char a = s[(i + k) % n];
        char b = s[(j + k) % n];
        if (a == b) ++k;
        else {
            if (a > b) i += k + 1;
            else j += k + 1;
            if (i == j) ++j;
            k = 0;
        }
    }
    return i < j ? i : j;
}

static void canonicalRotate(char* s, int n) {
    if (n <= 1) return;
    int r = leastRotation(s, n);
    if (r == 0) return;
    char* tmp = (char*)malloc((size_t)n + 1);
    memcpy(tmp, s + r, (size_t)(n - r));
    memcpy(tmp + (n - r), s, (size_t)r);
    tmp[n] = '\0';
    memcpy(s, tmp, (size_t)n + 1);
    free(tmp);
}

static int cmpstr(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

int minimumGroups(char** words, int wordsSize) {
    char** keys = (char**)malloc((size_t)wordsSize * sizeof(char*));
    for (int w = 0; w < wordsSize; w++) {
        int n = (int)strlen(words[w]);
        int ne = (n + 1) / 2, no = n / 2;
        char* even = (char*)malloc((size_t)ne + 1);
        char* odd = (char*)malloc((size_t)no + 1);
        int ei = 0, oi = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) even[ei++] = words[w][i];
            else odd[oi++] = words[w][i];
        }
        even[ei] = odd[oi] = '\0';
        canonicalRotate(even, ei);
        canonicalRotate(odd, oi);
        keys[w] = (char*)malloc((size_t)ei + oi + 2);
        memcpy(keys[w], even, (size_t)ei);
        keys[w][ei] = '#';
        memcpy(keys[w] + ei + 1, odd, (size_t)oi + 1);
        free(even);
        free(odd);
    }
    qsort(keys, (size_t)wordsSize, sizeof(char*), cmpstr);
    int groups = 0;
    for (int i = 0; i < wordsSize; i++) {
        if (i == 0 || strcmp(keys[i], keys[i - 1]) != 0) ++groups;
    }
    for (int i = 0; i < wordsSize; i++) free(keys[i]);
    free(keys);
    return groups;
}
