// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

#include <stdlib.h>
#include <string.h>

static int cmpDesc2982(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int maximumLength(char* s) {
    int n = (int)strlen(s);
    int* groups[26];
    int gsize[26] = {0};
    int gcap[26] = {0};
    for (int c = 0; c < 26; c++) groups[c] = NULL;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        int c = s[i] - 'a';
        if (gsize[c] == gcap[c]) {
            gcap[c] = gcap[c] ? gcap[c] * 2 : 4;
            groups[c] = (int*)realloc(groups[c], (size_t)gcap[c] * sizeof(int));
        }
        groups[c][gsize[c]++] = j - i;
        i = j;
    }
    int ans = -1;
    for (int c = 0; c < 26; c++) {
        if (gsize[c] == 0) continue;
        qsort(groups[c], (size_t)gsize[c], sizeof(int), cmpDesc2982);
        for (int L = groups[c][0]; L >= 1; L--) {
            int cnt = 0;
            for (int gi = 0; gi < gsize[c]; gi++) {
                if (groups[c][gi] >= L) cnt += groups[c][gi] - L + 1;
            }
            if (cnt >= 3) {
                if (L > ans) ans = L;
                break;
            }
        }
    }
    for (int c = 0; c < 26; c++) free(groups[c]);
    return ans;
}
