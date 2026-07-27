// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

#include <stdlib.h>
#include <string.h>

char** commonChars(char** words, int wordsSize, int* returnSize) {
    int common[26];
    for (int i = 0; i < 26; i++) common[i] = 100;
    for (int w = 0; w < wordsSize; w++) {
        int cnt[26] = {0};
        for (char* p = words[w]; *p; p++) cnt[*p - 'a']++;
        for (int i = 0; i < 26; i++)
            if (cnt[i] < common[i]) common[i] = cnt[i];
    }
    int total = 0;
    for (int i = 0; i < 26; i++) total += common[i];
    char** ans = (char**)malloc((size_t)total * sizeof(char*));
    *returnSize = 0;
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < common[i]; j++) {
            ans[*returnSize] = (char*)malloc(2);
            ans[*returnSize][0] = (char)('a' + i);
            ans[*returnSize][1] = '\0';
            (*returnSize)++;
        }
    }
    return ans;
}
