// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

#include <string.h>
#include <stdbool.h>

int minimumOperations(char* num) {
    int n = (int)strlen(num);
    int ans = n;
    bool has0 = false;
    for (int i = 0; i < n; i++) if (num[i] == '0') has0 = true;
    if (has0 && n - 1 < ans) ans = n - 1;
    const char* targets[] = {"00", "25", "50", "75"};
    for (int t = 0; t < 4; t++) {
        int j = n - 1;
        while (j >= 0 && num[j] != targets[t][1]) j--;
        if (j < 0) continue;
        int i = j - 1;
        while (i >= 0 && num[i] != targets[t][0]) i--;
        if (i < 0) continue;
        int cand = n - i - 2;
        if (cand < ans) ans = cand;
    }
    return ans;
}
