// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

#include <stdbool.h>
#include <string.h>

bool canMakeSubsequence(char* str1, char* str2) {
    int j = 0, n2 = (int)strlen(str2);
    for (int i = 0; str1[i] && j < n2; i++) {
        char a = str1[i], b = str2[j];
        if (a == b || (a - 'a' + 1) % 26 == (b - 'a')) j++;
    }
    return j == n2;
}
