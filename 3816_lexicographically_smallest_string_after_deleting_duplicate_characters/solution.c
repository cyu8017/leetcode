// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/

#include <stdlib.h>
#include <string.h>

char* lexSmallestAfterDeletion(char* s) {
    int cnt[26] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) cnt[s[i] - 'a']++;
    char* stk = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        char c = s[i];
        while (top > 0 && stk[top - 1] > c && cnt[stk[top - 1] - 'a'] > 1) {
            cnt[stk[top - 1] - 'a']--;
            top--;
        }
        stk[top++] = c;
    }
    while (top > 0 && cnt[stk[top - 1] - 'a'] > 1) {
        cnt[stk[top - 1] - 'a']--;
        top--;
    }
    stk[top] = '\0';
    return stk;
}
