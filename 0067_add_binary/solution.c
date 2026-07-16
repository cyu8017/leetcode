// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

#include <stdlib.h>
#include <string.h>

char* addBinary(char* a, char* b) {
    int i = (int)strlen(a) - 1;
    int j = (int)strlen(b) - 1;
    int carry = 0;
    int bufsize = (int)strlen(a) + (int)strlen(b) + 2;
    char* buf = (char*)malloc((size_t)bufsize);
    int k = bufsize - 1;

    buf[k--] = '\0';

    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) {
            total += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            total += b[j] - '0';
            j--;
        }
        buf[k--] = (char)('0' + (total % 2));
        carry = total / 2;
    }

    char* result = (char*)malloc((size_t)(bufsize - k));
    strcpy(result, buf + k + 1);
    free(buf);
    return result;
}
