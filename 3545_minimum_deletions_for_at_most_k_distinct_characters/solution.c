// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

#include <stdlib.h>
#include <string.h>

static int cmp_asc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int minDeletion(char* s, int k) {
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    int freq[26], fc = 0;
    for (int i = 0; i < 26; i++) if (cnt[i]) freq[fc++] = cnt[i];
    if (fc <= k) return 0;
    qsort(freq, (size_t)fc, sizeof(int), cmp_asc);
    int del = 0;
    for (int i = 0; i < fc - k; i++) del += freq[i];
    return del;
}
