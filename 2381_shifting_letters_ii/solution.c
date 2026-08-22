// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

#include <stdlib.h>
#include <string.h>

char* shiftingLetters(char* s, int** shifts, int shiftsSize, int* shiftsColSize) {
    (void)shiftsColSize;
    int n = (int)strlen(s);
    int* diff = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < shiftsSize; i++) {
        int d = shifts[i][2] == 0 ? -1 : 1;
        diff[shifts[i][0]] += d;
        diff[shifts[i][1] + 1] -= d;
    }
    char* b = (char*)malloc((size_t)(n + 1));
    strcpy(b, s);
    int cur = 0;
    for (int i = 0; i < n; i++) {
        cur = (cur + diff[i]) % 26;
        if (cur < 0) cur += 26;
        b[i] = (char)('a' + (b[i] - 'a' + cur) % 26);
    }
    free(diff);
    return b;
}
