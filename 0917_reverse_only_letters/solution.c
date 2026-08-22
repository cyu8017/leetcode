// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

#include <ctype.h>
#include <string.h>

char* reverseOnlyLetters(char* s) {
    int i = 0, j = (int)strlen(s) - 1;
    while (i < j) {
        while (i < j && !isalpha((unsigned char)s[i])) i++;
        while (i < j && !isalpha((unsigned char)s[j])) j--;
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
        i++;
        j--;
    }
    return s;
}
