// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isVowel(char c) {
    return c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
}
static int cmp_char(const void* a, const void* b) {
    return *(const unsigned char*)a - *(const unsigned char*)b;
}

char* sortVowels(char* s) {
    int n = (int)strlen(s);
    char* vowels = (char*)malloc(n + 1);
    int vc = 0;
    for (int i = 0; i < n; i++) if (isVowel(s[i])) vowels[vc++] = s[i];
    qsort(vowels, vc, 1, cmp_char);
    char* b = (char*)malloc(n + 1);
    strcpy(b, s);
    int vi = 0;
    for (int i = 0; i < n; i++) if (isVowel(b[i])) b[i] = vowels[vi++];
    free(vowels);
    return b;
}
