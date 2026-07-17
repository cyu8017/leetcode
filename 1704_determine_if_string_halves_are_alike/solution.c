// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

#include <stdbool.h>
#include <string.h>

static bool isVowel(char ch) {
    return strchr("aeiouAEIOU", ch) != NULL && ch != '\0';
}

bool halvesAreAlike(char* s) {
    int n = (int)strlen(s);
    int mid = n / 2;
    int balance = 0;
    for (int i = 0; i < n; i++) {
        if (isVowel(s[i])) {
            balance += i < mid ? 1 : -1;
        }
    }
    return balance == 0;
}
