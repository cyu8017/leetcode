// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

#include <stdlib.h>
#include <string.h>

long long sumScores(char* s) {
    int n = (int)strlen(s);
    int* z = (int*)calloc((size_t)n, sizeof(int));
    int l = 0, r = 0;
    for (int i = 1; i < n; i++) {
        if (i <= r) {
            z[i] = z[i - l];
            if (r - i + 1 < z[i]) z[i] = r - i + 1;
        }
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    long long ans = n;
    for (int i = 1; i < n; i++) ans += z[i];
    free(z);
    return ans;
}
