// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

char* greatestLetter(char* s) {
    bool lower[26] = {0}, upper[26] = {0};
    for (int i = 0; s[i]; i++) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') lower[c - 'a'] = true;
        else upper[c - 'A'] = true;
    }
    char* res = (char*)calloc(2, 1);
    for (int i = 25; i >= 0; i--) {
        if (lower[i] && upper[i]) {
            res[0] = (char)('A' + i);
            break;
        }
    }
    return res;
}
