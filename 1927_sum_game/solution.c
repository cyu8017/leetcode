// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

#include <stdbool.h>
#include <string.h>

static int score(char* s, int len) {
    int dig = 0, q = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '?') q++;
        else dig += s[i] - '0';
    }
    return dig * 2 + q * 9;
}

bool sumGame(char* num) {
    int n = (int)strlen(num);
    int half = n / 2;
    return score(num, half) != score(num + half, half);
}
