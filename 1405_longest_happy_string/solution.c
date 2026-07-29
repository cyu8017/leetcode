// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

#include <stdlib.h>

char* longestDiverseString(int a, int b, int c) {
    int cnt[3] = {a, b, c};
    char* ans = (char*)malloc(a + b + c + 1);
    int len = 0;
    while (1) {
        int order[3] = {0, 1, 2};
        for (int i = 0; i < 3; i++)
            for (int j = i + 1; j < 3; j++)
                if (cnt[order[j]] > cnt[order[i]]) {
                    int t = order[i]; order[i] = order[j]; order[j] = t;
                }
        int picked = -1;
        for (int t = 0; t < 3; t++) {
            int i = order[t];
            if (cnt[i] == 0) continue;
            if (len >= 2 && ans[len - 1] == 'a' + i && ans[len - 2] == 'a' + i) continue;
            picked = i;
            break;
        }
        if (picked < 0) break;
        ans[len++] = 'a' + picked;
        cnt[picked]--;
    }
    ans[len] = '\0';
    return ans;
}
