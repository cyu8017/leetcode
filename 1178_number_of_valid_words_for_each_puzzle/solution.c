// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

#include <stdlib.h>
#include <string.h>

static int maskOf(char* s) {
    int mask = 0;
    for (; *s; s++) mask |= 1 << (*s - 'a');
    return mask;
}

int* findNumOfValidWords(char** words, int wordsSize, char** puzzles, int puzzlesSize, int* returnSize) {
    // map mask -> count using open addressing
    int cap = 1;
    while (cap < wordsSize * 2 + 16) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)calloc((size_t)cap, sizeof(int));
    for (int i = 0; i < cap; i++) keys[i] = -1;
    for (int i = 0; i < wordsSize; i++) {
        int m = maskOf(words[i]);
        int idx = m & (cap - 1);
        while (keys[idx] != -1 && keys[idx] != m) idx = (idx + 1) & (cap - 1);
        keys[idx] = m;
        vals[idx]++;
    }
    int* ans = (int*)malloc((size_t)puzzlesSize * sizeof(int));
    for (int p = 0; p < puzzlesSize; p++) {
        int first = 1 << (puzzles[p][0] - 'a');
        int full = maskOf(puzzles[p]);
        int sub = full, total = 0;
        while (1) {
            if (sub & first) {
                int idx = sub & (cap - 1);
                while (keys[idx] != -1) {
                    if (keys[idx] == sub) { total += vals[idx]; break; }
                    idx = (idx + 1) & (cap - 1);
                }
            }
            if (sub == 0) break;
            sub = (sub - 1) & full;
        }
        ans[p] = total;
    }
    free(keys); free(vals);
    *returnSize = puzzlesSize;
    return ans;
}
