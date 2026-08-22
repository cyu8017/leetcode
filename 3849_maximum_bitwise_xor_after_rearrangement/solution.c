// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

#include <stdlib.h>
#include <string.h>

char* maximumXor(char* s, char* t) {
    int cnt[2] = {0, 0};
    for (int i = 0; t[i]; i++) cnt[t[i] - '0']++;
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        int x = s[i] - '0';
        if (cnt[x ^ 1] > 0) { cnt[x ^ 1]--; ans[i] = '1'; }
        else { cnt[x]--; ans[i] = '0'; }
    }
    ans[n] = '\0';
    return ans;
}
