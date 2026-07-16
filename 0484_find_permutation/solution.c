// LeetCode 0484 - Find Permutation
// https://leetcode.com/problems/find-permutation/

#include <stdlib.h>
#include <string.h>

int* findPermutation(char* s, int* returnSize) {
    int length = (int)strlen(s) + 1;
    int* stack = (int*)malloc((size_t)length * sizeof(int));
    int stackSize = 0;
    int* result = (int*)malloc((size_t)length * sizeof(int));
    int resultSize = 0;
    stack[stackSize++] = 1;
    for (int index = 0; s[index] != '\0'; index++) {
        if (s[index] == 'I') {
            while (stackSize > 0) {
                result[resultSize++] = stack[--stackSize];
            }
        }
        stack[stackSize++] = stackSize + resultSize;
    }
    while (stackSize > 0) {
        result[resultSize++] = stack[--stackSize];
    }
    free(stack);
    *returnSize = resultSize;
    return result;
}
