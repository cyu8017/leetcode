// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

#include <stdlib.h>
#include <string.h>

char* finalString(char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc(n + 1);
    int len = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'i') {
            for (int l = 0, r = len - 1; l < r; l++, r--) {
                char t = b[l]; b[l] = b[r]; b[r] = t;
            }
        } else b[len++] = s[i];
    }
    b[len] = 0;
    return b;
}
