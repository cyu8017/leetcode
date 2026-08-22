// LeetCode 0043 - Multiply Strings
// https://leetcode.com/problems/multiply-strings/

#include <stdlib.h>
#include <string.h>

char* multiply(char* num1, char* num2) {
    if (strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0) {
        char* result = (char*)malloc(2);
        strcpy(result, "0");
        return result;
    }

    int m = (int)strlen(num1);
    int n = (int)strlen(num2);
    int* positions = (int*)calloc((size_t)(m + n), sizeof(int));

    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int product = (num1[i] - '0') * (num2[j] - '0');
            int low = i + j + 1;
            int high = i + j;
            int total = product + positions[low];
            positions[low] = total % 10;
            positions[high] += total / 10;
        }
    }

    int start = 0;
    while (start < m + n - 1 && positions[start] == 0) {
        start++;
    }

    int result_len = m + n - start;
    char* result = (char*)malloc((size_t)result_len + 1);
    for (int k = start; k < m + n; k++) {
        result[k - start] = (char)('0' + positions[k]);
    }
    result[result_len] = '\0';

    free(positions);
    return result;
}
