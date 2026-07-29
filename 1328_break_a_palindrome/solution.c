// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

#include <stdlib.h>
#include <string.h>

char* breakPalindrome(char* palindrome) {
    int n = (int)strlen(palindrome);
    char* ans = (char*)malloc(n + 1);
    if (n == 1) { ans[0] = '\0'; return ans; }
    strcpy(ans, palindrome);
    for (int i = 0; i < n / 2; i++) {
        if (ans[i] != 'a') { ans[i] = 'a'; return ans; }
    }
    ans[n - 1] = 'b';
    return ans;
}
