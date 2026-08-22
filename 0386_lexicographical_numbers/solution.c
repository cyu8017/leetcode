// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

#include <stdlib.h>

static void dfsLexical(int current, int n, int* result, int* index) {
    if (current > n) {
        return;
    }
    result[(*index)++] = current;
    dfsLexical(current * 10, n, result, index);
    if (current % 10 < 9) {
        dfsLexical(current + 1, n, result, index);
    }
}

int* lexicalOrder(int n, int* returnSize) {
    int* result = (int*)malloc((size_t)n * sizeof(int));
    int index = 0;
    dfsLexical(1, n, result, &index);
    *returnSize = index;
    return result;
}
