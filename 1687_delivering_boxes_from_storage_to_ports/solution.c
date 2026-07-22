// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

#include <stdlib.h>

int boxDelivering(int** boxes, int boxesSize, int* boxesColSize, int portsCount, int maxBoxes, int maxWeight) {
    (void)boxesColSize; (void)portsCount;
    int n = boxesSize;
    long long* w = (long long*)calloc((size_t)n + 1, sizeof(long long));
    int* changes = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) {
        w[i] = w[i - 1] + boxes[i - 1][1];
        changes[i] = changes[i - 1] + (i > 1 && boxes[i - 1][0] != boxes[i - 2][0]);
    }
    int* dp = (int*)calloc((size_t)n + 1, sizeof(int));
    int* q = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int head = 0, tail = 0;
    q[tail++] = 0;
    for (int i = 1; i <= n; i++) {
        while (head < tail && (i - q[head] > maxBoxes || w[i] - w[q[head]] > maxWeight)) head++;
        int j = q[head];
        dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
        if (i < n) {
            int val = dp[i] - changes[i + 1];
            while (head < tail && dp[q[tail - 1]] - changes[q[tail - 1] + 1] >= val) tail--;
            q[tail++] = i;
        }
    }
    int ans = dp[n];
    free(w); free(changes); free(dp); free(q);
    return ans;
}
