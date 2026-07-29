// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

#include <stdbool.h>
#include <stdlib.h>

bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize) {
    (void)poppedSize;
    int* stack = (int*)malloc((size_t)pushedSize * sizeof(int));
    int top = 0, j = 0;
    for (int i = 0; i < pushedSize; i++) {
        stack[top++] = pushed[i];
        while (top > 0 && stack[top - 1] == popped[j]) { top--; j++; }
    }
    free(stack);
    return top == 0;
}
