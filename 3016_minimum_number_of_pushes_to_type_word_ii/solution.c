// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

#include <stdlib.h>
#include <string.h>

static int cmp_int(const void* a, const void* b) {
    return (*(const int*)a) - (*(const int*)b);
}

int minimumPushes(char* word) {
    int cnt[26] = {0};
    for (int i = 0; word[i]; i++) cnt[word[i] - 'a']++;
    qsort(cnt, 26, sizeof(int), cmp_int);
    int ans = 0;
    for (int i = 0; i < 26; i++) ans += (i / 8 + 1) * cnt[25 - i];
    return ans;
}
