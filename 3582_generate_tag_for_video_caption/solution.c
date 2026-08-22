// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

char* generateTag(char* caption) {
    char* ans = (char*)calloc(101, 1);
    int len = 0;
    ans[len++] = '#';
    bool firstWord = true;
    int n = (int)strlen(caption);
    int i = 0;
    while (i < n && len < 100) {
        while (i < n && isspace((unsigned char)caption[i])) i++;
        if (i >= n) break;
        int start = i;
        while (i < n && !isspace((unsigned char)caption[i])) i++;
        for (int j = start; j < i && len < 100; j++) {
            char c = (char)tolower((unsigned char)caption[j]);
            if (!firstWord && j == start) c = (char)toupper((unsigned char)c);
            ans[len++] = c;
        }
        firstWord = false;
    }
    ans[len] = '\0';
    return ans;
}
