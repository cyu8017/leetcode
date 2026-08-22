// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

#include <stdlib.h>
#include <string.h>

int minMovesToMakePalindrome(char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + 1);
    memcpy(b, s, (size_t)n + 1);
    int ans = 0, len = n;
    while (len > 1) {
        int j = len - 1;
        while (j > 0 && b[j] != b[0]) j--;
        if (j == 0) {
            ans += len / 2;
            memmove(b, b + 1, (size_t)(len - 1));
            len--;
            continue;
        }
        ans += len - 1 - j;
        memmove(b + j, b + j + 1, (size_t)(len - j - 1));
        len--;
        memmove(b, b + 1, (size_t)(len - 1));
        len--;
    }
    free(b);
    return ans;
}
