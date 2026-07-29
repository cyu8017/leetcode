// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * typedef struct Master Master;
 * int guess(struct Master* master, char* word);
 */

#include <stdlib.h>
#include <string.h>

static int match(const char* a, const char* b) {
    int m = 0;
    for (int i = 0; i < 6; i++) if (a[i] == b[i]) m++;
    return m;
}

void findSecretWord(char** words, int wordsSize, Master* master) {
    char** cand = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int nc = wordsSize;
    for (int i = 0; i < wordsSize; i++) cand[i] = words[i];
    while (nc > 0) {
        int best_i = 0, best_worst = nc + 1;
        for (int i = 0; i < nc; i++) {
            int buckets[7] = {0};
            for (int j = 0; j < nc; j++) buckets[match(cand[i], cand[j])]++;
            int worst = 0;
            for (int m = 0; m < 7; m++) if (buckets[m] > worst) worst = buckets[m];
            if (worst < best_worst) { best_worst = worst; best_i = i; }
        }
        char* guess_w = cand[best_i];
        int score = guess(master, guess_w);
        if (score == 6) { free(cand); return; }
        int nn = 0;
        for (int i = 0; i < nc; i++)
            if (match(cand[i], guess_w) == score) cand[nn++] = cand[i];
        nc = nn;
    }
    free(cand);
}
