// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

#include <stdlib.h>

int minGroupsForValidAssignment(int* balls, int ballsSize) {
    /* count frequencies via sort */
    int* a = (int*)malloc(ballsSize * sizeof(int));
    for (int i = 0; i < ballsSize; i++) a[i] = balls[i];
    for (int i = 0; i < ballsSize; i++)
        for (int j = i + 1; j < ballsSize; j++)
            if (a[j] < a[i]) { int t = a[i]; a[i] = a[j]; a[j] = t; }
    int* counts = (int*)malloc(ballsSize * sizeof(int));
    int cn = 0, minF = 1 << 30;
    for (int i = 0; i < ballsSize; ) {
        int j = i;
        while (j < ballsSize && a[j] == a[i]) j++;
        counts[cn++] = j - i;
        if (j - i < minF) minF = j - i;
        i = j;
    }
    free(a);
    for (int size = minF; size >= 1; size--) {
        int ok = 1, groups = 0;
        for (int i = 0; i < cn; i++) {
            int c = counts[i];
            int rem = c % (size + 1);
            int g2 = c / (size + 1);
            if (rem == 0) groups += g2;
            else if (size - rem <= g2) groups += g2 + 1;
            else { ok = 0; break; }
        }
        if (ok) { free(counts); return groups; }
    }
    free(counts);
    return ballsSize;
}
