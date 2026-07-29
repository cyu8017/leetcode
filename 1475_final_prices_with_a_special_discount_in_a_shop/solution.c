// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

#include <stdlib.h>

int* finalPrices(int* prices, int pricesSize, int* returnSize) {
    int* ans = (int*)malloc(pricesSize * sizeof(int));
    for (int i = 0; i < pricesSize; i++) ans[i] = prices[i];
    int* stack = (int*)malloc(pricesSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < pricesSize; i++) {
        while (top && prices[stack[top - 1]] >= prices[i]) {
            int j = stack[--top];
            ans[j] -= prices[i];
        }
        stack[top++] = i;
    }
    free(stack);
    *returnSize = pricesSize;
    return ans;
}
