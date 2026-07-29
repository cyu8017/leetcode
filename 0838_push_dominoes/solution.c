// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

#include <stdlib.h>
#include <string.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

char* pushDominoes(char* dominoes) {
    int n = (int)strlen(dominoes);
    int* force = (int*)calloc((size_t)n, sizeof(int));
    int f = 0;
    for (int i = 0; i < n; i++) {
        if (dominoes[i] == 'R') f = n;
        else if (dominoes[i] == 'L') f = 0;
        else f = MAX(f - 1, 0);
        force[i] += f;
    }
    f = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (dominoes[i] == 'L') f = n;
        else if (dominoes[i] == 'R') f = 0;
        else f = MAX(f - 1, 0);
        force[i] -= f;
    }
    char* ans = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++)
        ans[i] = force[i] > 0 ? 'R' : (force[i] < 0 ? 'L' : '.');
    ans[n] = '\0';
    free(force);
    return ans;
}
