// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

#include <stdlib.h>
#include <string.h>
#include <limits.h>

typedef struct Trie {
    struct Trie* next[26];
} Trie;

static Trie* newTrie(void) {
    return (Trie*)calloc(1, sizeof(Trie));
}

static void freeTrie(Trie* t) {
    if (!t) return;
    for (int i = 0; i < 26; i++) freeTrie(t->next[i]);
    free(t);
}

int minValidStrings(char** words, int wordsSize, char* target) {
    int n = (int)strlen(target);
    const int INF = INT_MAX / 4;
    int* dp = (int*)malloc((size_t)(n + 1) * sizeof(int));
    dp[0] = 0;
    for (int i = 1; i <= n; i++) dp[i] = INF;
    Trie* root = newTrie();
    for (int wi = 0; wi < wordsSize; wi++) {
        Trie* cur = root;
        for (int j = 0; words[wi][j]; j++) {
            int ci = words[wi][j] - 'a';
            if (!cur->next[ci]) cur->next[ci] = newTrie();
            cur = cur->next[ci];
        }
    }
    for (int i = 0; i < n; i++) {
        if (dp[i] == INF) continue;
        Trie* cur = root;
        for (int j = i; j < n; j++) {
            int ci = target[j] - 'a';
            if (!cur->next[ci]) break;
            cur = cur->next[ci];
            if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1;
        }
    }
    int ans = dp[n] == INF ? -1 : dp[n];
    free(dp); freeTrie(root);
    return ans;
}
