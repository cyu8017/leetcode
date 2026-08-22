// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

#include <stdlib.h>
#include <string.h>

char* answerString(char* word, int numFriends) {
    int n = (int)strlen(word);
    if (numFriends == 1) {
        char* r = (char*)malloc(n + 1); strcpy(r, word); return r;
    }
    int maxLen = n - (numFriends - 1);
    char* ans = (char*)calloc(1, 1);
    for (int i = 0; i < n; i++) {
        int end = i + maxLen; if (end > n) end = n;
        int len = end - i;
        char* cand = (char*)malloc(len + 1);
        memcpy(cand, word + i, len); cand[len] = 0;
        if (strcmp(cand, ans) > 0) { free(ans); ans = cand; }
        else free(cand);
    }
    return ans;
}
