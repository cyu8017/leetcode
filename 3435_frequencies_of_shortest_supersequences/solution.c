// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

#include <stdlib.h>
#include <string.h>

static char** g_words; static int g_wn;
static int g_letters[26]; static int g_m;
static int g_best;
static int** g_bestFreqs; static int g_bn, g_bcap;

static void dfs3435(int i, int freq[26]) {
    if (i == g_m) {
        for (int w = 0; w < g_wn; w++) {
            int a = g_words[w][0] - 'a', b = g_words[w][1] - 'a';
            if (a == b) { if (freq[a] < 2) return; }
            else if (freq[a] < 1 || freq[b] < 1) return;
        }
        int sum = 0; for (int j = 0; j < 26; j++) sum += freq[j];
        if (sum < g_best) {
            g_best = sum; g_bn = 0;
            if (g_bn == g_bcap) { g_bcap = g_bcap ? g_bcap * 2 : 4; g_bestFreqs = (int**)realloc(g_bestFreqs, g_bcap * sizeof(int*)); }
            /* reset */
            for (int k = 0; k < g_bn; k++) free(g_bestFreqs[k]);
            g_bn = 0;
        }
        if (sum == g_best) {
            if (g_bn == g_bcap) { g_bcap = g_bcap ? g_bcap * 2 : 4; g_bestFreqs = (int**)realloc(g_bestFreqs, g_bcap * sizeof(int*)); }
            g_bestFreqs[g_bn] = (int*)malloc(26 * sizeof(int));
            memcpy(g_bestFreqs[g_bn], freq, 26 * sizeof(int));
            g_bn++;
        }
        return;
    }
    int L = g_letters[i];
    for (int c = 1; c <= 2; c++) { freq[L] = c; dfs3435(i + 1, freq); }
    freq[L] = 0;
}

int** supersequences(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    g_words = words; g_wn = wordsSize;
    int used[26] = {0}; g_m = 0;
    for (int i = 0; i < wordsSize; i++) { used[words[i][0] - 'a'] = 1; used[words[i][1] - 'a'] = 1; }
    for (int i = 0; i < 26; i++) if (used[i]) g_letters[g_m++] = i;
    g_best = 1000000000; g_bestFreqs = NULL; g_bn = 0; g_bcap = 0;
    int freq[26] = {0};
    dfs3435(0, freq);
    *returnSize = g_bn;
    *returnColumnSizes = (int*)malloc(g_bn * sizeof(int));
    for (int i = 0; i < g_bn; i++) (*returnColumnSizes)[i] = 26;
    return g_bestFreqs;
}
