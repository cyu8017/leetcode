// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

#include <stdlib.h>
#include <string.h>

static void removeAt(int* numbers, int* size, int index) {
    for (int i = index + 1; i < *size; i++) {
        numbers[i - 1] = numbers[i];
    }
    (*size)--;
}

char* getPermutation(int n, int k) {
    int* numbers = (int*)malloc((size_t)n * sizeof(int));
    int* factorials = (int*)malloc((size_t)n * sizeof(int));
    factorials[0] = 1;

    for (int i = 0; i < n; i++) {
        numbers[i] = i + 1;
        if (i > 0) {
            factorials[i] = factorials[i - 1] * i;
        }
    }

    k--;
    char* result = (char*)malloc((size_t)(n + 1));
    int resultLen = 0;
    int size = n;

    for (int i = n - 1; i >= 0; i--) {
        int index = k / factorials[i];
        result[resultLen++] = (char)('0' + numbers[index]);
        removeAt(numbers, &size, index);
        k %= factorials[i];
    }

    result[resultLen] = '\0';
    free(numbers);
    free(factorials);
    return result;
}
