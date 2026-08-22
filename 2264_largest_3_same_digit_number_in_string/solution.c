// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

#include <stdlib.h>
#include <string.h>

char* largestGoodInteger(char* num) {
    char* best = (char*)calloc(4, sizeof(char));
    int n = (int)strlen(num);
    for (int i = 0; i + 2 < n; i++) {
        if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
            char cand[4] = {num[i], num[i + 1], num[i + 2], '\0'};
            if (strcmp(cand, best) > 0) {
                strcpy(best, cand);
            }
        }
    }
    return best;
}
