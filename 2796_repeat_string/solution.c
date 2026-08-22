// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/

#include <stdlib.h>
#include <string.h>

char* replicate(char* str, int times) {
    if (times <= 0) {
        char* r = (char*)malloc(1);
        r[0] = 0;
        return r;
    }
    int len = (int)strlen(str);
    char* b = (char*)malloc((size_t)len * times + 1);
    for (int i = 0; i < times; i++) memcpy(b + (size_t)i * len, str, len);
    b[(size_t)len * times] = 0;
    return b;
}
