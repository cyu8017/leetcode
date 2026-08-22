// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

#include <stdlib.h>
#include <string.h>

char* smallestSubsequence(char* s, int k, char letter, int repetition) {
    int n = (int)strlen(s);
    int remainLetter = 0;
    for (int i = 0; i < n; i++) if (s[i] == letter) remainLetter++;
    char* stack = (char*)malloc((size_t)k + 1);
    int top = 0, inStackLetter = 0;
    for (int i = 0; i < n; i++) {
        char ch = s[i];
        while (top > 0 && ch < stack[top - 1] && top + n - i > k) {
            char t = stack[top - 1];
            if (t == letter) {
                if (inStackLetter + remainLetter - 1 < repetition) break;
                inStackLetter--;
            }
            top--;
        }
        if (top < k) {
            if (ch == letter) { stack[top++] = ch; inStackLetter++; }
            else if (k - top > repetition - inStackLetter) stack[top++] = ch;
        }
        if (ch == letter) remainLetter--;
    }
    stack[top] = '\0';
    return stack;
}
