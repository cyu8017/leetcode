// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

#include <stdlib.h>
#include <string.h>

static int cmp_desc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int minimumKeypresses(char* s) {
    int freq[26] = {0};
    for (int i = 0; s[i]; i++) freq[s[i] - 'a']++;
    qsort(freq, 26, sizeof(int), cmp_desc);
    int ans = 0;
    for (int i = 0; i < 26; i++) {
        if (freq[i] == 0) break;
        ans += freq[i] * (i / 9 + 1);
    }
    return ans;
}
