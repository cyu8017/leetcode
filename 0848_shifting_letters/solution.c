// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

#include <stdlib.h>
#include <string.h>

char* shiftingLetters(char* s, int* shifts, int shiftsSize) {
    int n = shiftsSize;
    char* ans = (char*)malloc((size_t)n + 1);
    strcpy(ans, s);
    int total = 0;
    for (int i = n - 1; i >= 0; i--) {
        total = (total + shifts[i]) % 26;
        ans[i] = (char)((ans[i] - 'a' + total) % 26 + 'a');
    }
    return ans;
}
