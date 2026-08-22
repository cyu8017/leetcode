// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

#include <stdlib.h>
#include <string.h>

char* decodeCiphertext(char* encodedText, int rows) {
    int len = (int)strlen(encodedText);
    if (rows == 1) {
        char* ans = (char*)malloc((size_t)len + 1);
        strcpy(ans, encodedText);
        return ans;
    }
    int cols = len / rows;
    char* b = (char*)malloc((size_t)len + 1);
    int bn = 0;
    for (int c = 0; c < cols; c++) {
        for (int r = 0; r < rows && c + r < cols; r++) {
            b[bn++] = encodedText[r * cols + c + r];
        }
    }
    while (bn > 0 && b[bn - 1] == ' ') bn--;
    b[bn] = '\0';
    return b;
}
