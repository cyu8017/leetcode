// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

#include <stdlib.h>
#include <string.h>

static int is_vowel(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

char* trimTrailingVowels(char* s) {
    int n = (int)strlen(s);
    int i = n - 1;
    while (i >= 0 && is_vowel(s[i])) i--;
    char* out = (char*)malloc((size_t)(i + 2));
    memcpy(out, s, (size_t)(i + 1));
    out[i + 1] = '\0';
    return out;
}
