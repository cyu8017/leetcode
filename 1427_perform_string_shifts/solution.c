// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

#include <stdlib.h>
#include <string.h>

char* stringShift(char* s, int** shift, int shiftSize, int* shiftColSize) {
    (void)shiftColSize;
    int n = (int)strlen(s);
    int offset = 0;
    for (int i = 0; i < shiftSize; i++)
        offset += shift[i][0] ? shift[i][1] : -shift[i][1];
    offset %= n;
    if (offset < 0) offset += n;
    char* ans = (char*)malloc(n + 1);
    if (offset == 0) { strcpy(ans, s); return ans; }
    memcpy(ans, s + (n - offset), offset);
    memcpy(ans + offset, s, n - offset);
    ans[n] = '\0';
    return ans;
}
