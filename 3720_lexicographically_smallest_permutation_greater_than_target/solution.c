// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int cnt[26];
static char* ans;
static char* target;
static int n;

static bool dfs(int pos, bool greater) {
    if (pos == n) return greater;
    int start = greater ? 0 : (target[pos] - 'a');
    for (int c = start; c < 26; c++) {
        if (cnt[c] == 0) continue;
        cnt[c]--;
        ans[pos] = (char)('a' + c);
        bool ng = greater || (c > target[pos] - 'a');
        if (dfs(pos + 1, ng)) return true;
        cnt[c]++;
    }
    return false;
}

char* lexGreaterPermutation(char* s, char* targetStr) {
    memset(cnt, 0, sizeof(cnt));
    n = (int)strlen(s);
    target = targetStr;
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    ans = (char*)malloc((size_t)(n + 1));
    ans[n] = 0;
    if (dfs(0, false)) return ans;
    free(ans);
    char* empty = (char*)malloc(1);
    empty[0] = 0;
    return empty;
}
