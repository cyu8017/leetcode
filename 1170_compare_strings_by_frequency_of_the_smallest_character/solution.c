// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

#include <stdlib.h>
#include <string.h>

static int f(char* s) {
    char mn = 'z';
    for (char* p = s; *p; p++) if (*p < mn) mn = *p;
    int c = 0;
    for (char* p = s; *p; p++) if (*p == mn) c++;
    return c;
}

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int* numSmallerByFrequency(char** queries, int queriesSize, char** words, int wordsSize, int* returnSize) {
    int* freqs = (int*)malloc((size_t)wordsSize * sizeof(int));
    for (int i = 0; i < wordsSize; i++) freqs[i] = f(words[i]);
    qsort(freqs, (size_t)wordsSize, sizeof(int), cmpInt);
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int qf = f(queries[i]);
        int lo = 0, hi = wordsSize;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (freqs[mid] <= qf) lo = mid + 1; else hi = mid;
        }
        ans[i] = wordsSize - lo;
    }
    free(freqs);
    *returnSize = queriesSize;
    return ans;
}
