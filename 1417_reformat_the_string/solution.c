// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* reformat(char* s) {
    int n = (int)strlen(s);
    char* letters = (char*)malloc(n + 1);
    char* digits = (char*)malloc(n + 1);
    int ln = 0, dn = 0;
    for (int i = 0; i < n; i++) {
        if (isalpha((unsigned char)s[i])) letters[ln++] = s[i];
        else digits[dn++] = s[i];
    }
    char* ans = (char*)malloc(n + 1);
    if (ln - dn > 1 || dn - ln > 1) { ans[0] = '\0'; free(letters); free(digits); return ans; }
    char *a = letters, *b = digits;
    int an = ln, bn = dn;
    if (bn > an) { a = digits; b = letters; an = dn; bn = ln; }
    int idx = 0;
    for (int i = 0; i < an; i++) {
        ans[idx++] = a[i];
        if (i < bn) ans[idx++] = b[i];
    }
    ans[idx] = '\0';
    free(letters); free(digits);
    return ans;
}
