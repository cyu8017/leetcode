// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

#include <stdlib.h>
#include <string.h>

int numberOfPermutations(int n, int** requirements, int requirementsSize, int* requirementsColSize) {
    (void)requirementsColSize;
    int* req = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) req[i] = -1;
    for (int i = 0; i < requirementsSize; i++) req[requirements[i][0]] = requirements[i][1];
    if (req[0] > 0) { free(req); return 0; }
    req[0] = 0;
    int m = 0;
    for (int i = 0; i < n; i++) if (req[i] > m) m = req[i];
    const int mod = 1000000007;
    int* f = calloc(n * (m + 1), sizeof(int));
    f[0] = 1;
    for (int i = 1; i < n; i++) {
        int l = 0, r = m;
        if (req[i] >= 0) { l = r = req[i]; }
        for (int j = l; j <= r; j++) {
            int lim = i < j ? i : j;
            for (int k = 0; k <= lim; k++)
                f[i * (m + 1) + j] = (f[i * (m + 1) + j] + f[(i - 1) * (m + 1) + (j - k)]) % mod;
        }
    }
    int ans = f[(n - 1) * (m + 1) + req[n - 1]];
    free(req); free(f);
    return ans;
}
