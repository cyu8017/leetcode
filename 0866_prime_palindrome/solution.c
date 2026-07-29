// LeetCode 0866 - Prime Palindrome
// https://leetcode.com/problems/prime-palindrome/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static bool is_prime(int x) {
    if (x < 2) return false;
    if (x % 2 == 0) return x == 2;
    for (int d = 3; d * d <= x; d += 2)
        if (x % d == 0) return false;
    return true;
}

static int make_pal(int root) {
    char s[16], pal[16];
    sprintf(s, "%d", root);
    int len = (int)strlen(s);
    strcpy(pal, s);
    for (int i = len - 2; i >= 0; i--) {
        char tmp[2] = {s[i], 0};
        strcat(pal, tmp);
    }
    return atoi(pal);
}

int primePalindrome(int n) {
    if (n <= 2) return 2;
    if (n <= 3) return 3;
    if (n <= 5) return 5;
    if (n <= 7) return 7;
    if (n <= 11) return 11;
    for (int length = 1; length <= 5; length++) {
        int start = 1;
        for (int i = 1; i < length; i++) start *= 10;
        int end = start * 10;
        for (int root = start; root < end; root++) {
            int pal = make_pal(root);
            if (pal >= n && is_prime(pal)) return pal;
        }
    }
    return 0;
}
