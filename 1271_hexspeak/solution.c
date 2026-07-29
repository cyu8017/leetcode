// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

#include <stdlib.h>
#include <string.h>

char* toHexspeak(char* num) {
    unsigned long long value = strtoull(num, NULL, 10);
    if (value == 0) {
        char* ans = (char*)malloc(2);
        ans[0] = 'O';
        ans[1] = '\0';
        return ans;
    }
    char digits[] = "0123456789ABCDEF";
    char rev[32];
    int len = 0;
    while (value) {
        int rem = (int)(value % 16);
        if (rem >= 2 && rem <= 9) {
            char* err = (char*)malloc(6);
            strcpy(err, "ERROR");
            return err;
        }
        rev[len++] = digits[rem];
        value /= 16;
    }
    char* ans = (char*)malloc((size_t)len + 1);
    for (int i = 0; i < len; i++) {
        char ch = rev[len - 1 - i];
        if (ch == '0') ch = 'O';
        else if (ch == '1') ch = 'I';
        ans[i] = ch;
    }
    ans[len] = '\0';
    return ans;
}
