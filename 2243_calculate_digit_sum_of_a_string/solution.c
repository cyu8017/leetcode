// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* digitSum(char* s, int k) {
    char* cur = strdup(s);
    while ((int)strlen(cur) > k) {
        int n = (int)strlen(cur);
        char* next = (char*)malloc((size_t)n * 2 + 8);
        next[0] = '\0';
        for (int i = 0; i < n; i += k) {
            int end = i + k;
            if (end > n) end = n;
            int sum = 0;
            for (int j = i; j < end; j++) sum += cur[j] - '0';
            char buf[16];
            sprintf(buf, "%d", sum);
            strcat(next, buf);
        }
        free(cur);
        cur = next;
    }
    return cur;
}
