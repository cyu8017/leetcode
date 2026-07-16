// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int n = (int)strlen(s);
    if (numRows == 1 || numRows >= n) {
        char* copy = (char*)malloc((size_t)n + 1);
        strcpy(copy, s);
        return copy;
    }

    char** rows = (char**)malloc((size_t)numRows * sizeof(char*));
    int* lengths = (int*)calloc((size_t)numRows, sizeof(int));
    for (int i = 0; i < numRows; i++) {
        rows[i] = (char*)malloc((size_t)n + 1);
        rows[i][0] = '\0';
    }

    int index = 0;
    int step = 1;
    for (int i = 0; i < n; i++) {
        rows[index][lengths[index]++] = s[i];
        rows[index][lengths[index]] = '\0';
        if (index == 0) {
            step = 1;
        } else if (index == numRows - 1) {
            step = -1;
        }
        index += step;
    }

    char* result = (char*)malloc((size_t)n + 1);
    result[0] = '\0';
    for (int i = 0; i < numRows; i++) {
        strcat(result, rows[i]);
        free(rows[i]);
    }
    free(rows);
    free(lengths);
    return result;
}
