// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* largestTimeFromDigits(int* arr, int arrSize) {
    (void)arrSize;
    char* best = (char*)calloc(6, 1);
    int p[24][4];
    int n = 0;
    for (int a = 0; a < 4; a++)
        for (int b = 0; b < 4; b++) if (b != a)
            for (int c = 0; c < 4; c++) if (c != a && c != b) {
                int d = 6 - a - b - c;
                p[n][0]=a; p[n][1]=b; p[n][2]=c; p[n][3]=d; n++;
            }
    for (int i = 0; i < n; i++) {
        int h = 10 * arr[p[i][0]] + arr[p[i][1]];
        int m = 10 * arr[p[i][2]] + arr[p[i][3]];
        if (h < 24 && m < 60) {
            char cand[6];
            sprintf(cand, "%02d:%02d", h, m);
            if (strcmp(cand, best) > 0) strcpy(best, cand);
        }
    }
    return best;
}
