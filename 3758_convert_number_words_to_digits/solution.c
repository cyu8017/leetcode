// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

#include <stdlib.h>
#include <string.h>

char* convertNumber(char* s) {
    const char* d[] = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)(n + 1));
    int p = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 10; j++) {
            int m = (int)strlen(d[j]);
            if (i + m <= n && strncmp(s + i, d[j], (size_t)m) == 0) {
                ans[p++] = (char)('0' + j);
                i += m - 1;
                break;
            }
        }
    }
    ans[p] = 0;
    return ans;
}
