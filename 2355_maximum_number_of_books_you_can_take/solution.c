// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

#include <stdlib.h>

static long long shelfSum(int l, int r, int h) {
    int width = r - l + 1;
    if (h >= width) return (long long)width * (2LL * h - width + 1) / 2;
    return (long long)h * (h + 1) / 2;
}

long long maximumBooks(int* books, int booksSize) {
    int n = booksSize;
    long long* dp = (long long*)malloc((size_t)n * sizeof(long long));
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && books[stack[top - 1]] >= books[i] - (i - stack[top - 1])) top--;
        if (top == 0) dp[i] = shelfSum(0, i, books[i]);
        else {
            int j = stack[top - 1];
            dp[i] = dp[j] + shelfSum(j + 1, i, books[i]);
        }
        if (dp[i] > ans) ans = dp[i];
        stack[top++] = i;
    }
    free(dp); free(stack);
    return ans;
}
