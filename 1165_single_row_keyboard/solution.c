// LeetCode 1165 - Single-Row Keyboard
// https://leetcode.com/problems/single-row-keyboard/

#include <stdlib.h>

int calculateTime(char* keyboard, char* word) {
    int pos[26];
    for (int i = 0; keyboard[i]; i++) pos[keyboard[i] - 'a'] = i;
    int ans = 0, prev = 0;
    for (int i = 0; word[i]; i++) {
        int p = pos[word[i] - 'a'];
        ans += abs(p - prev);
        prev = p;
    }
    return ans;
}
