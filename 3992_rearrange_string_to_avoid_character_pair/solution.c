// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

#include <string.h>

char* rearrangeString(char* s, char x, char y) {
    (void)x;
    int n = (int)strlen(s);
    int i = 0;
    for (int j = 0; j < n; j++) {
        if (s[j] == y) {
            char tmp = s[i];
            s[i] = s[j];
            s[j] = tmp;
            i++;
        }
    }
    return s;
}
