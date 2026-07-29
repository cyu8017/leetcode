// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

#include <stdlib.h>

struct CustomFunction {
    int (*f)(int, int);
};

int** findSolution(struct CustomFunction* customfunction, int z, int* returnSize, int** returnColumnSizes) {
    int** answer = (int**)malloc(2000 * sizeof(int*));
    int count = 0;
    int x = 1;
    int y = 1000;
    while (x <= 1000 && y >= 1) {
        int value = customfunction->f(x, y);
        if (value == z) {
            answer[count] = (int*)malloc(2 * sizeof(int));
            answer[count][0] = x;
            answer[count][1] = y;
            count++;
            x++;
            y--;
        } else if (value < z) x++;
        else y--;
    }
    *returnSize = count;
    *returnColumnSizes = (int*)malloc((size_t)count * sizeof(int));
    for (int i = 0; i < count; i++) (*returnColumnSizes)[i] = 2;
    answer = (int**)realloc(answer, (size_t)count * sizeof(int*));
    return answer;
}
