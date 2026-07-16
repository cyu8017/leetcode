// LeetCode 0072 - Edit Distance
// https://leetcode.com/problems/edit-distance/

#include <stdlib.h>
#include <string.h>

static int min3(int a, int b, int c) {
    if (a <= b && a <= c) {
        return a;
    }
    if (b <= a && b <= c) {
        return b;
    }
    return c;
}

int minDistance(char* word1, char* word2) {
    int m = (int)strlen(word1);
    int n = (int)strlen(word2);
    int* prev = (int*)malloc((n + 1) * sizeof(int));
    int* curr = (int*)malloc((n + 1) * sizeof(int));

    for (int j = 0; j <= n; j++) {
        prev[j] = j;
    }

    for (int i = 1; i <= m; i++) {
        curr[0] = i;
        for (int j = 1; j <= n; j++) {
            if (word1[i - 1] == word2[j - 1]) {
                curr[j] = prev[j - 1];
            } else {
                curr[j] = 1 + min3(prev[j], curr[j - 1], prev[j - 1]);
            }
        }
        int* tmp = prev;
        prev = curr;
        curr = tmp;
    }

    int result = prev[n];
    free(prev);
    free(curr);
    return result;
}
