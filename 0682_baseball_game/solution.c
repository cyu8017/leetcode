// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

#include <stdlib.h>
#include <string.h>

int calPoints(char** operations, int operationsSize) {
    int* stack = (int*)malloc((size_t)operationsSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < operationsSize; i++) {
        char* op = operations[i];
        if (strcmp(op, "+") == 0) {
            stack[top] = stack[top - 1] + stack[top - 2];
            top++;
        } else if (strcmp(op, "D") == 0) {
            stack[top] = 2 * stack[top - 1];
            top++;
        } else if (strcmp(op, "C") == 0) {
            top--;
        } else {
            stack[top++] = atoi(op);
        }
    }
    int sum = 0;
    for (int i = 0; i < top; i++) sum += stack[i];
    free(stack);
    return sum;
}
