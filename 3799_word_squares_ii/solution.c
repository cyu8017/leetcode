// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

#include <stdlib.h>
#include <string.h>

static int cmp_str(const void* a, const void* b) {
    return strcmp(*(char* const*)a, *(char* const*)b);
}

char*** wordSquares(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    qsort(words, (size_t)wordsSize, sizeof(char*), cmp_str);
    int n = wordsSize;
    int cap = n * n * n;
    if (cap < 8) cap = 8;
    char*** ans = (char***)malloc((size_t)cap * sizeof(char**));
    int* cols = (int*)malloc((size_t)cap * sizeof(int));
    int asz = 0;
    for (int i = 0; i < n; i++) {
        char* top = words[i];
        for (int j = 0; j < n; j++) if (j != i) {
            char* left = words[j];
            for (int k = 0; k < n; k++) if (k != j && k != i) {
                char* right = words[k];
                for (int h = 0; h < n; h++) if (h != k && h != j && h != i) {
                    char* bottom = words[h];
                    if (top[0] == left[0] && top[3] == right[0] && bottom[0] == left[3] && bottom[3] == right[3]) {
                        if (asz == cap) {
                            cap *= 2;
                            ans = (char***)realloc(ans, (size_t)cap * sizeof(char**));
                            cols = (int*)realloc(cols, (size_t)cap * sizeof(int));
                        }
                        char** row = (char**)malloc(4 * sizeof(char*));
                        row[0] = top; row[1] = left; row[2] = right; row[3] = bottom;
                        ans[asz] = row;
                        cols[asz] = 4;
                        asz++;
                    }
                }
            }
        }
    }
    *returnSize = asz;
    *returnColumnSizes = cols;
    return ans;
}
