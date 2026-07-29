// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

#include <stdlib.h>
#include <string.h>

char* removeVowels(char* s) {
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    int j = 0;
    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') continue;
        ans[j++] = c;
    }
    ans[j] = '\0';
    return ans;
}
