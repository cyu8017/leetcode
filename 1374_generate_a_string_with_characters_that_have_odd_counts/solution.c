// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

#include <stdlib.h>

char* generateTheString(int n) {
    char* s = (char*)malloc(n + 1);
    for (int i = 0; i < n; i++) s[i] = 'a';
    if (n % 2 == 0) s[n - 1] = 'b';
    s[n] = '\0';
    return s;
}
