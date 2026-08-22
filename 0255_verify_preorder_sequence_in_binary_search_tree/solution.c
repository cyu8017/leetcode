// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

#include <limits.h>
#include <stdbool.h>
#include <stdlib.h>

bool verifyPreorder(int* preorder, int preorderSize) {
    long low = LONG_MIN;
    int* stack = (int*)malloc((size_t)preorderSize * sizeof(int));
    int size = 0;

    for (int index = 0; index < preorderSize; index++) {
        int value = preorder[index];
        if (value < low) {
            free(stack);
            return false;
        }
        while (size > 0 && stack[size - 1] < value) {
            low = stack[--size];
        }
        stack[size++] = value;
    }

    free(stack);
    return true;
}
