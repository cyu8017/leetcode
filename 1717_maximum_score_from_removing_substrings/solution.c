// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

#include <stdlib.h>
#include <string.h>

static int removePair(const char* text, char open, char close, int score, char* rest) {
    int gained = 0;
    int top = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (top > 0 && rest[top - 1] == open && ch == close) {
            top--;
            gained += score;
        } else {
            rest[top++] = ch;
        }
    }
    rest[top] = '\0';
    return gained;
}

int maximumGain(char* s, int x, int y) {
    size_t len = strlen(s);
    char* rest = (char*)malloc(len + 1);
    char* rest2 = (char*)malloc(len + 1);
    int first;
    int second;
    if (x >= y) {
        first = removePair(s, 'a', 'b', x, rest);
        second = removePair(rest, 'b', 'a', y, rest2);
    } else {
        first = removePair(s, 'b', 'a', y, rest);
        second = removePair(rest, 'a', 'b', x, rest2);
    }
    free(rest);
    free(rest2);
    return first + second;
}
