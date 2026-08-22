// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

#include <stdlib.h>
#include <string.h>

char* removeDigit(char* number, char digit) {
    int n = (int)strlen(number);
    char* best = (char*)calloc((size_t)n, sizeof(char));
    char* cand = (char*)malloc((size_t)n);
    for (int i = 0; i < n; i++) {
        if (number[i] == digit) {
            memcpy(cand, number, (size_t)i);
            memcpy(cand + i, number + i + 1, (size_t)(n - i - 1));
            cand[n - 1] = '\0';
            if (strcmp(cand, best) > 0) {
                strcpy(best, cand);
            }
        }
    }
    free(cand);
    return best;
}
