// LeetCode 0412 - Fizz Buzz
// https://leetcode.com/problems/fizz-buzz/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** fizzBuzz(int n, int* returnSize) {
    char** result = (char**)malloc((size_t)n * sizeof(char*));
    *returnSize = n;

    for (int value = 1; value <= n; value++) {
        if (value % 15 == 0) {
            result[value - 1] = strdup("FizzBuzz");
        } else if (value % 3 == 0) {
            result[value - 1] = strdup("Fizz");
        } else if (value % 5 == 0) {
            result[value - 1] = strdup("Buzz");
        } else {
            char buffer[16];
            snprintf(buffer, sizeof(buffer), "%d", value);
            result[value - 1] = strdup(buffer);
        }
    }

    return result;
}
