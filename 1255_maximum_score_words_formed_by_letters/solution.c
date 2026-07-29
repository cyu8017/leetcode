// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

#include <stdlib.h>
#include <string.h>

static int dfs(
    char** words,
    int wordsSize,
    int* values,
    int (*counts)[26],
    int* available,
    int index
) {
    if (index == wordsSize) return 0;
    int best = dfs(words, wordsSize, values, counts, available, index + 1);
    int ok = 1;
    for (int c = 0; c < 26; c++) {
        if (counts[index][c] > available[c]) {
            ok = 0;
            break;
        }
    }
    if (ok) {
        for (int c = 0; c < 26; c++) available[c] -= counts[index][c];
        int val = values[index] + dfs(words, wordsSize, values, counts, available, index + 1);
        if (val > best) best = val;
        for (int c = 0; c < 26; c++) available[c] += counts[index][c];
    }
    return best;
}

int maxScoreWords(char** words, int wordsSize, char* letters, int* score) {
    int available[26] = {0};
    for (int i = 0; letters[i]; i++) available[letters[i] - 'a']++;
    int* values = (int*)malloc((size_t)wordsSize * sizeof(int));
    int (*counts)[26] = (int (*)[26])malloc((size_t)wordsSize * 26 * sizeof(int));
    for (int i = 0; i < wordsSize; i++) {
        memset(counts[i], 0, sizeof(counts[i]));
        values[i] = 0;
        for (int j = 0; words[i][j]; j++) {
            counts[i][words[i][j] - 'a']++;
            values[i] += score[words[i][j] - 'a'];
        }
    }
    int ans = dfs(words, wordsSize, values, counts, available, 0);
    free(values);
    free(counts);
    return ans;
}
