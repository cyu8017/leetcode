// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

#include <stdlib.h>
#include <string.h>

int minOperations(char* initial, char* target) {
    int m = (int)strlen(initial), n = (int)strlen(target);
    int* f = calloc((m + 1) * (n + 1), sizeof(int));
    int mx = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (initial[i] == target[j]) {
                f[(i + 1) * (n + 1) + (j + 1)] = f[i * (n + 1) + j] + 1;
                if (f[(i + 1) * (n + 1) + (j + 1)] > mx) mx = f[(i + 1) * (n + 1) + (j + 1)];
            }
        }
    }
    free(f);
    return m + n - 2 * mx;
}
