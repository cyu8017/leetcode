// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* decodeAtIndex(char* s, int k) {
    long long size = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        if (isdigit((unsigned char)s[i])) size *= s[i] - '0';
        else size++;
    }
    char* ans = (char*)malloc(2);
    ans[1] = '\0';
    long long kk = k;
    for (int i = n - 1; i >= 0; i--) {
        if (size > 0) kk %= size;
        if (kk == 0 && isalpha((unsigned char)s[i])) {
            ans[0] = s[i];
            return ans;
        }
        if (isdigit((unsigned char)s[i])) size /= s[i] - '0';
        else size--;
    }
    ans[0] = '\0';
    return ans;
}
