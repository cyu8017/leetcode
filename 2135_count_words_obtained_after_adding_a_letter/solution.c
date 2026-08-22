// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int wordMask(char* w) {
    int m = 0;
    for (int i = 0; w[i]; i++) m |= 1 << (w[i] - 'a');
    return m;
}

int wordCount(char** startWords, int startWordsSize, char** targetWords, int targetWordsSize) {
    // masks fit in 2^26; use hash set of ints
    int cap = 1 << 16;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    bool* used = (bool*)calloc((size_t)cap, sizeof(bool));
    for (int i = 0; i < startWordsSize; i++) {
        int m = wordMask(startWords[i]);
        unsigned h = (unsigned)m % (unsigned)cap;
        for (;;) {
            if (!used[h]) { used[h] = true; keys[h] = m; break; }
            if (keys[h] == m) break;
            h = (h + 1) % (unsigned)cap;
        }
    }
    int ans = 0;
    for (int t = 0; t < targetWordsSize; t++) {
        int m = wordMask(targetWords[t]);
        int len = (int)strlen(targetWords[t]);
        for (int i = 0; i < len; i++) {
            int need = m ^ (1 << (targetWords[t][i] - 'a'));
            unsigned h = (unsigned)need % (unsigned)cap;
            int found = 0;
            for (;;) {
                if (!used[h]) break;
                if (keys[h] == need) { found = 1; break; }
                h = (h + 1) % (unsigned)cap;
            }
            if (found) { ans++; break; }
        }
    }
    free(keys); free(used);
    return ans;
}
