// LeetCode 1499 - Max Value of Equation
// https://leetcode.com/problems/max-value-of-equation/

#include <stdlib.h>

int findMaxValueOfEquation(int** points, int pointsSize, int* pointsColSize, int k) {
    (void)pointsColSize;
    int* qx = (int*)malloc(pointsSize * sizeof(int));
    int* qv = (int*)malloc(pointsSize * sizeof(int));
    int head = 0, tail = 0;
    int ans = -2000000000;
    for (int i = 0; i < pointsSize; i++) {
        int x = points[i][0], y = points[i][1];
        while (head < tail && x - qx[head] > k) head++;
        if (head < tail) {
            int cand = x + y + qv[head];
            if (cand > ans) ans = cand;
        }
        int value = y - x;
        while (head < tail && qv[tail - 1] <= value) tail--;
        qx[tail] = x; qv[tail] = value; tail++;
    }
    free(qx); free(qv);
    return ans;
}
