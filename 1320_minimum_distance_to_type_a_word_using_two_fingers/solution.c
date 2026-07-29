// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

#include <string.h>
#include <stdlib.h>

static int dist(int a, int b) {
    if (a == 26) return 0;
    return abs(a / 6 - b / 6) + abs(a % 6 - b % 6);
}

int minimumDistance(char* word) {
    int n = (int)strlen(word);
    if (n <= 1) return 0;
    int* letters = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) letters[i] = word[i] - 'A';
    int INF = 1000000000;
    int dp[27], nxt[27];
    for (int i = 0; i < 27; i++) dp[i] = INF;
    dp[26] = 0;
    int previous = letters[0];
    for (int t = 1; t < n; t++) {
        int current = letters[t];
        for (int i = 0; i < 27; i++) nxt[i] = INF;
        for (int free = 0; free < 27; free++) {
            if (dp[free] >= INF) continue;
            int c1 = dp[free] + dist(previous, current);
            if (c1 < nxt[free]) nxt[free] = c1;
            int c2 = dp[free] + dist(free, current);
            if (c2 < nxt[previous]) nxt[previous] = c2;
        }
        for (int i = 0; i < 27; i++) dp[i] = nxt[i];
        previous = current;
    }
    int ans = INF;
    for (int i = 0; i < 27; i++) if (dp[i] < ans) ans = dp[i];
    free(letters);
    return ans;
}
