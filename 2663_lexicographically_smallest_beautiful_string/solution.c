// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

#include <stdlib.h>
#include <string.h>

char* smallestBeautifulString(char* s, int k) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + 1);
    memcpy(b, s, (size_t)n + 1);
    for (int i = n - 1; i >= 0; i--) {
        for (char c = (char)(b[i] + 1); c < (char)('a' + k); c++) {
            if ((i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2])) continue;
            b[i] = c;
            for (int j = i + 1; j < n; j++) {
                for (char nc = 'a'; nc < (char)('a' + k); nc++) {
                    if ((j > 0 && nc == b[j - 1]) || (j > 1 && nc == b[j - 2])) continue;
                    b[j] = nc;
                    break;
                }
            }
            return b;
        }
    }
    free(b);
    char* empty = (char*)malloc(1);
    empty[0] = '\0';
    return empty;
}
