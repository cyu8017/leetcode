// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

#include <string.h>

static int roman_value(char ch) {
    switch (ch) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}

int romanToInt(char* s) {
    int total = 0;
    int prev = 0;
    int n = (int)strlen(s);

    for (int i = n - 1; i >= 0; i--) {
        int curr = roman_value(s[i]);
        if (curr < prev) {
            total -= curr;
        } else {
            total += curr;
        }
        prev = curr;
    }

    return total;
}
