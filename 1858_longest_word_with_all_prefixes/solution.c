// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

#include <stdlib.h>
#include <string.h>

static int wordInSet(char** words, int wordsSize, const char* prefix, int len) {
    for (int i = 0; i < wordsSize; i++) {
        if ((int)strlen(words[i]) == len && strncmp(words[i], prefix, (size_t)len) == 0) {
            return 1;
        }
    }
    return 0;
}

char* longestWord(char** words, int wordsSize) {
    char* best = (char*)calloc(1, sizeof(char));
    int bestLen = 0;
    for (int i = 0; i < wordsSize; i++) {
        char* word = words[i];
        int len = (int)strlen(word);
        int valid = 1;
        for (int L = len; L >= 1; L--) {
            if (!wordInSet(words, wordsSize, word, L)) {
                valid = 0;
                break;
            }
        }
        if (valid && (len > bestLen || (len == bestLen && strcmp(word, best) < 0))) {
            free(best);
            best = (char*)malloc((size_t)len + 1);
            memcpy(best, word, (size_t)len + 1);
            bestLen = len;
        }
    }
    return best;
}
