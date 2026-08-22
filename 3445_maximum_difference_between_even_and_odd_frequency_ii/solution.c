// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

#include <stdlib.h>
#include <string.h>

int maxDifference(char* s, int k) {
    int n = (int)strlen(s), ans = -1000000000;
    for (int a = 0; a < 5; a++) for (int b = 0; b < 5; b++) {
        if (a == b) continue;
        int* prefA = (int*)calloc(n + 1, sizeof(int));
        int* prefB = (int*)calloc(n + 1, sizeof(int));
        for (int i = 0; i < n; i++) {
            prefA[i + 1] = prefA[i] + (s[i] - '0' == a);
            prefB[i + 1] = prefB[i] + (s[i] - '0' == b);
        }
        for (int i = 0; i < n; i++) for (int j = i + k - 1; j < n; j++) {
            int fa = prefA[j + 1] - prefA[i];
            int fb = prefB[j + 1] - prefB[i];
            if (fa % 2 == 1 && fb % 2 == 0 && fb > 0 && fa - fb > ans) ans = fa - fb;
        }
        free(prefA); free(prefB);
    }
    return ans;
}
