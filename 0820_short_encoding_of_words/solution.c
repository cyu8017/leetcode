// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minimumLengthEncoding(char** words, int wordsSize) {
    bool keep[200] = {0};
    for (int i = 0; i < wordsSize; i++) keep[i] = true;
    for (int i = 0; i < wordsSize; i++) {
        int len = (int)strlen(words[i]);
        for (int j = 0; j < wordsSize; j++) {
            if (!keep[j] || i == j) continue;
            int lj = (int)strlen(words[j]);
            if (lj < len) continue;
            if (strcmp(words[j] + lj - len, words[i]) == 0) {
                keep[i] = false;
                break;
            }
        }
    }
    // also remove proper suffixes of same word via original algorithm
    // rebuild using set-like: discard suffixes
    // simpler: for each word discard its own suffixes against kept set
    char* good[200];
    int ng = 0;
    for (int i = 0; i < wordsSize; i++) {
        bool dup = false;
        for (int j = 0; j < ng; j++) if (strcmp(good[j], words[i]) == 0) { dup = true; break; }
        if (!dup) good[ng++] = words[i];
    }
    bool alive[200];
    for (int i = 0; i < ng; i++) alive[i] = true;
    for (int i = 0; i < ng; i++) {
        int len = (int)strlen(good[i]);
        for (int s = 1; s < len; s++) {
            const char* suf = good[i] + s;
            for (int j = 0; j < ng; j++) {
                if (strcmp(good[j], suf) == 0) alive[j] = false;
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < ng; i++) if (alive[i]) ans += (int)strlen(good[i]) + 1;
    return ans;
}
