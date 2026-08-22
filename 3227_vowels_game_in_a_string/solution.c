// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

#include <stdbool.h>

bool doesAliceWin(char* s) {
    for (int i = 0; s[i]; i++) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') return true;
    }
    return false;
}
