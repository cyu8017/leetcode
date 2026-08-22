// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

#include <stdbool.h>
#include <string.h>

bool makeStringsEqual(char* s, char* target) {
    bool has1s = false, has1t = false;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '1') has1s = true;
        if (target[i] == '1') has1t = true;
    }
    return has1s == has1t;
}
