// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int half[26];
static char* left;
static char* target;
static int halfLen, midCh;

static bool dfs(int pos, bool greater) {
    if (pos == halfLen) {
        if (midCh >= 0) {
            if (greater) return true;
            return (char)('a' + midCh) > target[halfLen];
        }
        return greater;
    }
    int start = greater ? 0 : (target[pos] - 'a');
    for (int c = start; c < 26; c++) {
        if (half[c] == 0) continue;
        half[c]--;
        left[pos] = (char)('a' + c);
        if (dfs(pos + 1, greater || c > target[pos] - 'a')) return true;
        half[c]++;
    }
    return false;
}

char* lexPalindromicPermutation(char* s, char* targetStr) {
    int cnt[26] = {0};
    int n = (int)strlen(s);
    target = targetStr;
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    int odd = 0; midCh = -1;
    for (int i = 0; i < 26; i++) if (cnt[i] % 2 == 1) { odd++; midCh = i; }
    if (odd > 1) { char* e=(char*)malloc(1); e[0]=0; return e; }
    for (int i = 0; i < 26; i++) half[i] = cnt[i] / 2;
    halfLen = n / 2;
    left = (char*)malloc((size_t)(halfLen + 1));
    if (!dfs(0, false)) { free(left); char* e=(char*)malloc(1); e[0]=0; return e; }
    char* res = (char*)malloc((size_t)(n + 1));
    int p = 0;
    for (int i = 0; i < halfLen; i++) res[p++] = left[i];
    if (midCh >= 0) res[p++] = (char)('a' + midCh);
    for (int i = halfLen - 1; i >= 0; i--) res[p++] = left[i];
    res[p] = 0;
    free(left);
    if (strcmp(res, target) <= 0) { free(res); char* e=(char*)malloc(1); e[0]=0; return e; }
    return res;
}
