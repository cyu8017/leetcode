// LeetCode 1209 - Remove All Adjacent Duplicates in String II
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

#include <stdlib.h>
#include <string.h>

char* removeDuplicates(char* s, int k) {
    int n = (int)strlen(s);
    char* chars = (char*)malloc((size_t)n);
    int* counts = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (top > 0 && chars[top - 1] == s[i]) counts[top - 1]++;
        else {
            chars[top] = s[i];
            counts[top] = 1;
            top++;
        }
        if (counts[top - 1] == k) top--;
    }
    int len = 0;
    for (int i = 0; i < top; i++) len += counts[i];
    char* ans = (char*)malloc((size_t)len + 1);
    int idx = 0;
    for (int i = 0; i < top; i++) {
        for (int j = 0; j < counts[i]; j++) ans[idx++] = chars[i];
    }
    ans[idx] = '\0';
    free(chars);
    free(counts);
    return ans;
}
