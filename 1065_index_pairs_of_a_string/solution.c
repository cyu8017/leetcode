// LeetCode 1065 - Index Pairs of a String
// https://leetcode.com/problems/index-pairs-of-a-string/

#include <stdlib.h>
#include <string.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** indexPairs(char* text, char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    int n = (int)strlen(text);
    int cap = 64;
    int** ans = (int**)malloc((size_t)cap * sizeof(int*));
    *returnColumnSizes = (int*)malloc((size_t)cap * sizeof(int));
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int len = j - i + 1;
            for (int w = 0; w < wordsSize; w++) {
                if ((int)strlen(words[w]) == len && strncmp(text + i, words[w], (size_t)len) == 0) {
                    if (count == cap) {
                        cap *= 2;
                        ans = (int**)realloc(ans, (size_t)cap * sizeof(int*));
                        *returnColumnSizes = (int*)realloc(*returnColumnSizes, (size_t)cap * sizeof(int));
                    }
                    ans[count] = (int*)malloc(2 * sizeof(int));
                    ans[count][0] = i;
                    ans[count][1] = j;
                    (*returnColumnSizes)[count] = 2;
                    count++;
                    break;
                }
            }
        }
    }
    *returnSize = count;
    return ans;
}
