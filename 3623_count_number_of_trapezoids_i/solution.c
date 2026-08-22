// LeetCode 3623 - Count Number of Trapezoids I
// https://leetcode.com/problems/count-number-of-trapezoids-i/

#include <stdlib.h>
int countTrapezoids(int** points, int pointsSize, int* pointsColSize) {
    (void)pointsColSize;
    /* count by y using sort */
    int* ys = (int*)malloc((size_t)pointsSize * sizeof(int));
    for (int i = 0; i < pointsSize; i++) ys[i] = points[i][1];
    for (int i = 0; i < pointsSize; i++) for (int j = i+1; j < pointsSize; j++)
        if (ys[j] < ys[i]) { int t=ys[i]; ys[i]=ys[j]; ys[j]=t; }
    const int mod = 1000000007;
    long long ans = 0, s = 0;
    for (int i = 0; i < pointsSize; ) {
        int j = i; while (j < pointsSize && ys[j] == ys[i]) j++;
        long long v = j - i;
        long long t = v * (v - 1) / 2;
        ans = (ans + s * t) % mod;
        s += t;
        i = j;
    }
    free(ys);
    return (int)ans;
}
