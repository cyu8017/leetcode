// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

#include <stdlib.h>

int clumsy(int n) {
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    stack[top++] = n;
    n--;
    int op = 0;
    while (n) {
        if (op % 4 == 0) {
            stack[top - 1] *= n;
        } else if (op % 4 == 1) {
            stack[top - 1] /= n;
        } else if (op % 4 == 2) {
            stack[top++] = n;
        } else {
            stack[top++] = -n;
        }
        n--;
        op++;
    }
    int sum = 0;
    for (int i = 0; i < top; i++) sum += stack[i];
    free(stack);
    return sum;
}
