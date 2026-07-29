// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

#include <string.h>

char* lastSubstring(char* s) {
    int i = 0, j = 1, k = 0, n = (int)strlen(s);
    while (j + k < n) {
        if (s[i + k] == s[j + k]) { k++; continue; }
        if (s[i + k] > s[j + k]) j = j + k + 1;
        else {
            int ni = i + k + 1;
            if (ni < j) ni = j;
            i = ni;
            j = i + 1;
        }
        k = 0;
    }
    return s + i;
}
