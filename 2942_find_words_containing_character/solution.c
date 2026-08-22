// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

#include <stdlib.h>
#include <string.h>

int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* ans = (int*)malloc(wordsSize * sizeof(int));
    int an = 0;
    for (int i = 0; i < wordsSize; i++) {
        for (int j = 0; words[i][j]; j++) {
            if (words[i][j] == x) { ans[an++] = i; break; }
        }
    }
    *returnSize = an;
    return ans;
}
