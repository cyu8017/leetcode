// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

#include <stdbool.h>
#include <string.h>

bool arrayStringsAreEqual(char** word1, int word1Size, char** word2, int word2Size) {
    int i1 = 0, j1 = 0, i2 = 0, j2 = 0;
    while (i1 < word1Size && i2 < word2Size) {
        if (word1[i1][j1] != word2[i2][j2]) return false;
        j1++; j2++;
        if (word1[i1][j1] == '\0') { i1++; j1 = 0; }
        if (word2[i2][j2] == '\0') { i2++; j2 = 0; }
    }
    return i1 == word1Size && i2 == word2Size;
}
