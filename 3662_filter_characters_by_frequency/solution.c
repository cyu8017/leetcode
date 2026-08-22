// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

#include <stdlib.h>
#include <string.h>
char* filterCharacters(char* s, int k) {
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    int len = 0;
    for (int i = 0; s[i]; i++) if (cnt[s[i] - 'a'] < k) ans[len++] = s[i];
    ans[len] = '\0';
    return ans;
}
