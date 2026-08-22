// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

#include <stdlib.h>
#include <stdbool.h>

struct InfiniteStream;
int InfiniteStreamNext(struct InfiniteStream* stream);

static int* getLPS(int* pattern, int n) {
    int* lps = (int*)calloc((size_t)n, sizeof(int));
    int j = 0;
    for (int i = 1; i < n; i++) {
        while (j > 0 && pattern[j] != pattern[i]) j = lps[j - 1];
        if (pattern[i] == pattern[j]) { j++; lps[i] = j; }
    }
    return lps;
}

int findPattern(struct InfiniteStream* stream, int* pattern, int patternSize) {
    int* lps = getLPS(pattern, patternSize);
    int i = 0, j = 0, bit = 0;
    bool readNext = false;
    for (;;) {
        if (!readNext) { bit = InfiniteStreamNext(stream); readNext = true; }
        if (bit == pattern[j]) {
            i++; readNext = false; j++;
            if (j == patternSize) { free(lps); return i - j; }
        } else if (j > 0) {
            j = lps[j - 1];
        } else {
            i++; readNext = false;
        }
    }
}
