// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

#include <stdlib.h>

int sumSubarrayMins(int* arr, int arrSize) {
    const int MOD = 1000000007;
    int* left = (int*)malloc((size_t)arrSize * sizeof(int));
    int* right = (int*)malloc((size_t)arrSize * sizeof(int));
    int* stack = (int*)malloc((size_t)arrSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < arrSize; i++) {
        while (top > 0 && arr[stack[top - 1]] > arr[i]) top--;
        left[i] = top > 0 ? stack[top - 1] : -1;
        stack[top++] = i;
    }
    top = 0;
    for (int i = arrSize - 1; i >= 0; i--) {
        while (top > 0 && arr[stack[top - 1]] >= arr[i]) top--;
        right[i] = top > 0 ? stack[top - 1] : arrSize;
        stack[top++] = i;
    }
    long long ans = 0;
    for (int i = 0; i < arrSize; i++) {
        ans = (ans + (long long)arr[i] * (i - left[i]) * (right[i] - i)) % MOD;
    }
    free(left);
    free(right);
    free(stack);
    return (int)ans;
}
