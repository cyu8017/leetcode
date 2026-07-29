// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

#include <stdlib.h>
#include <string.h>

char* maximumNumber(char* num, int* change, int changeSize) {
    (void)changeSize;
    int n = (int)strlen(num);
    char* chars = (char*)malloc((size_t)n + 1);
    memcpy(chars, num, (size_t)n + 1);
    int started = 0;
    for (int i = 0; i < n; i++) {
        int d = chars[i] - '0';
        int mapped = change[d];
        if (mapped > d) {
            chars[i] = (char)('0' + mapped);
            started = 1;
        } else if (mapped < d && started) {
            break;
        }
    }
    return chars;
}
