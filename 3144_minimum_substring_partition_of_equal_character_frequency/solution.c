// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

#include <stdlib.h>
#include <string.h>

static int* f3144;
static char* s3144;
static int n3144;

static int dfs3144(int i) {
    if (i >= n3144) return 0;
    if (f3144[i] != -1) return f3144[i];
    int cnt[26] = {0};
    int* freq = calloc(n3144 + 1, sizeof(int));
    int distinctFreq = 0;
    f3144[i] = n3144 - i;
    for (int j = i; j < n3144; j++) {
        int k = s3144[j] - 'a';
        if (cnt[k] > 0) {
            freq[cnt[k]]--;
            if (freq[cnt[k]] == 0) distinctFreq--;
        }
        cnt[k]++;
        if (freq[cnt[k]] == 0) distinctFreq++;
        freq[cnt[k]]++;
        if (distinctFreq == 1) {
            int v = 1 + dfs3144(j + 1);
            if (v < f3144[i]) f3144[i] = v;
        }
    }
    free(freq);
    return f3144[i];
}

int minimumSubstringsInPartition(char* s) {
    s3144 = s; n3144 = (int)strlen(s);
    f3144 = malloc(n3144 * sizeof(int));
    for (int i = 0; i < n3144; i++) f3144[i] = -1;
    int ans = dfs3144(0);
    free(f3144);
    return ans;
}
