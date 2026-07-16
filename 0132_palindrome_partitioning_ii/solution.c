// LeetCode 0132 - Palindrome Partitioning II
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
int minCut(char* s) {
    int n = strlen(s);
    bool *pal = calloc(n * n, sizeof(bool));
    int *cuts = malloc(n * sizeof(int));
    for (int i = n - 1; i >= 0; --i)
        for (int j = i; j < n; ++j)
            pal[i * n + j] = s[i] == s[j] && (j - i < 2 || pal[(i + 1) * n + j - 1]);
    for (int i = 0; i < n; ++i) {
        cuts[i] = i;
        for (int j = 0; j <= i; ++j)
            if (pal[j * n + i] && (j == 0 || cuts[j - 1] + 1 < cuts[i]))
                cuts[i] = j == 0 ? 0 : cuts[j - 1] + 1;
    }
    int answer = cuts[n - 1]; free(pal); free(cuts); return answer;
}