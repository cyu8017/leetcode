// LeetCode 3438 - Find Valid Pair of Adjacent Digits in String
// https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

#include <stdlib.h>
#include <string.h>

char* findValidPair(char* s) {
    int freq[10] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) freq[s[i] - '0']++;
    for (int i = 0; i + 1 < n; i++) {
        int a = s[i] - '0', b = s[i + 1] - '0';
        if (a != b && freq[a] == a && freq[b] == b) {
            char* r = (char*)malloc(3); r[0] = s[i]; r[1] = s[i + 1]; r[2] = 0; return r;
        }
    }
    char* r = (char*)malloc(1); r[0] = 0; return r;
}
