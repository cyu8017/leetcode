// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

#include <string.h>

int balancedStringSplit(char* s) {
    int balance = 0;
    int answer = 0;
    for (int i = 0; s[i]; i++) {
        balance += s[i] == 'L' ? 1 : -1;
        if (balance == 0) answer++;
    }
    return answer;
}
