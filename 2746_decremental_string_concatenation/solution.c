// LeetCode 2746 - Decremental String Concatenation
// https://leetcode.com/problems/decremental-string-concatenation/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

static char** words2746;
static int n2746;
static int memo2746[1001][26][26];
static char vis2746[1001][26][26];

static int dfs2746(int i, int first, int last) {
    if (i == n2746) return 0;
    if (vis2746[i][first][last]) return memo2746[i][first][last];
    vis2746[i][first][last] = 1;
    char* w = words2746[i];
    int len = (int)strlen(w);
    int wf = w[0] - 'a', wl = w[len - 1] - 'a';
    int add1 = len - (last == wf ? 1 : 0);
    int add2 = len - (wl == first ? 1 : 0);
    int a = add1 + dfs2746(i + 1, first, wl);
    int b = add2 + dfs2746(i + 1, wf, last);
    int best = a < b ? a : b;
    return memo2746[i][first][last] = best;
}

int minimizeConcatenatedLength(char** words, int wordsSize) {
    words2746 = words;
    n2746 = wordsSize;
    memset(vis2746, 0, sizeof(vis2746));
    char* w0 = words[0];
    int len0 = (int)strlen(w0);
    return len0 + dfs2746(1, w0[0] - 'a', w0[len0 - 1] - 'a');
}
