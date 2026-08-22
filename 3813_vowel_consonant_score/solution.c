// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

#include <ctype.h>
#include <string.h>

int vowelConsonantScore(char* s) {
    int v = 0, c = 0;
    for (int i = 0; s[i]; i++) {
        unsigned char ch = (unsigned char)s[i];
        if (isalpha(ch)) {
            c++;
            char lower = (char)tolower(ch);
            if (lower == 'a' || lower == 'e' || lower == 'i' || lower == 'o' || lower == 'u') v++;
        }
    }
    c -= v;
    if (c == 0) return 0;
    return v / c;
}
