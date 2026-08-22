// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

#include <stdlib.h>

int totalStrength(int* strength, int strengthSize) {
    const int mod = 1000000007;
    int n = strengthSize;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && strength[stack[top - 1]] >= strength[i]) top--;
        left[i] = top == 0 ? -1 : stack[top - 1];
        stack[top++] = i;
    }
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && strength[stack[top - 1]] > strength[i]) top--;
        right[i] = top == 0 ? n : stack[top - 1];
        stack[top++] = i;
    }
    long long* pref = (long long*)calloc((size_t)(n + 1), sizeof(long long));
    long long* prefPref = (long long*)calloc((size_t)(n + 2), sizeof(long long));
    for (int i = 0; i < n; i++) pref[i + 1] = (pref[i] + strength[i]) % mod;
    for (int i = 0; i <= n; i++) prefPref[i + 1] = (prefPref[i] + pref[i]) % mod;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        int l = left[i] + 1, r = right[i] - 1;
        long long leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod;
        long long rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod;
        long long leftCnt = i - l + 1;
        long long rightCnt = r - i + 1;
        long long contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod;
        ans = (ans + contrib * strength[i] % mod) % mod;
    }
    free(left); free(right); free(stack); free(pref); free(prefPref);
    return (int)ans;
}
