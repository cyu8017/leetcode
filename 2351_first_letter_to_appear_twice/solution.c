// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

#include <stdbool.h>

char repeatedCharacter(char* s) {
    bool seen[26] = {0};
    for (int i = 0; s[i]; i++) {
        int c = s[i] - 'a';
        if (seen[c]) return s[i];
        seen[c] = true;
    }
    return 0;
}
