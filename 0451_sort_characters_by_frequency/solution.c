// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char ch;
    int count;
} FreqPair;

static int cmpFreq(const void* a, const void* b) {
    const FreqPair* left = (const FreqPair*)a;
    const FreqPair* right = (const FreqPair*)b;
    if (left->count != right->count) {
        return right->count - left->count;
    }
    return (unsigned char)left->ch - (unsigned char)right->ch;
}

char* frequencySort(char* s) {
    int counts[256] = {0};
    int length = (int)strlen(s);
    for (int i = 0; i < length; i++) {
        counts[(unsigned char)s[i]]++;
    }

    FreqPair pairs[256];
    int pairCount = 0;
    for (int c = 0; c < 256; c++) {
        if (counts[c] > 0) {
            pairs[pairCount].ch = (char)c;
            pairs[pairCount].count = counts[c];
            pairCount++;
        }
    }
    qsort(pairs, (size_t)pairCount, sizeof(FreqPair), cmpFreq);

    char* result = (char*)malloc((size_t)length + 1);
    int pos = 0;
    for (int i = 0; i < pairCount; i++) {
        for (int j = 0; j < pairs[i].count; j++) {
            result[pos++] = pairs[i].ch;
        }
    }
    result[pos] = '\0';
    return result;
}
