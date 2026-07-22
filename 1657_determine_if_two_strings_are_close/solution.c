// LeetCode 1657 - Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

bool closeStrings(char* word1, char* word2) {
    int a[26] = {0}, b[26] = {0};
    for (char* p = word1; *p; p++) a[*p - 'a']++;
    for (char* p = word2; *p; p++) b[*p - 'a']++;
    for (int i = 0; i < 26; i++) {
        if ((a[i] == 0) != (b[i] == 0)) return false;
    }
    qsort(a, 26, sizeof(int), cmpInt);
    qsort(b, 26, sizeof(int), cmpInt);
    return memcmp(a, b, sizeof(a)) == 0;
}
