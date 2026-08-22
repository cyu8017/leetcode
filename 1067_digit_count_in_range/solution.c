// LeetCode 1067 - Digit Count in Range
// https://leetcode.com/problems/digit-count-in-range/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int ipow10(int e) {
    int p = 1;
    while (e-- > 0) {
        p *= 10;
    }
    return p;
}

static int countUpto(int d, int n) {
    if (n < 0) {
        return 0;
    }
    char s[16];
    sprintf(s, "%d", n);
    int length = (int)strlen(s);
    int ans = 0;
    for (int i = 0; i < length; i++) {
        int left = 0;
        for (int k = 0; k < i; k++) {
            left = left * 10 + (s[k] - '0');
        }
        int right = 0;
        for (int k = i + 1; k < length; k++) {
            right = right * 10 + (s[k] - '0');
        }
        int digit = s[i] - '0';
        int power = ipow10(length - i - 1);
        if (d != 0) {
            ans += left * power;
            if (digit > d) {
                ans += power;
            } else if (digit == d) {
                ans += right + 1;
            }
        } else {
            if (i == 0) {
                continue;
            }
            ans += (left - 1) * power;
            if (digit > 0) {
                ans += power;
            } else {
                ans += right + 1;
            }
        }
    }
    return ans;
}

int digitsCount(int d, int low, int high) {
    return countUpto(d, high) - countUpto(d, low - 1);
}
