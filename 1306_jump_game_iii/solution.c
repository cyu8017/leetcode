// LeetCode 1306 - Jump Game III
// https://leetcode.com/problems/jump-game-iii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool canReach(int* arr, int arrSize, int start) {
    char* seen = (char*)calloc(arrSize, 1);
    int* stack = (int*)malloc(arrSize * sizeof(int));
    int top = 0;
    stack[top++] = start;
    while (top > 0) {
        int i = stack[--top];
        if (i < 0 || i >= arrSize || seen[i]) continue;
        if (arr[i] == 0) { free(seen); free(stack); return true; }
        seen[i] = 1;
        stack[top++] = i - arr[i];
        stack[top++] = i + arr[i];
    }
    free(seen); free(stack);
    return false;
}
