// LeetCode 0784 - Letter Case Permutation
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char** letterCasePermutation(char* s, int* returnSize) {
    int n = (int)strlen(s), letters = 0;
    for (int i = 0; i < n; i++) if (isalpha((unsigned char)s[i])) letters++;
    int total = 1 << letters;
    char** result = (char**)malloc((size_t)total * sizeof(char*));
    for (int mask = 0; mask < total; mask++) {
        result[mask] = (char*)malloc((size_t)n + 1);
        int bit = 0;
        for (int i = 0; i < n; i++) {
            if (isalpha((unsigned char)s[i])) {
                char base = (char)tolower((unsigned char)s[i]);
                result[mask][i] = (mask & (1 << bit)) ? (char)toupper((unsigned char)base) : base;
                bit++;
            } else result[mask][i] = s[i];
        }
        result[mask][n] = '\0';
    }
    *returnSize = total;
    return result;
}
