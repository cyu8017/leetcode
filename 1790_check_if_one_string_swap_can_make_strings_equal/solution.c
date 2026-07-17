// LeetCode 1790 - Check if One String Swap Can Make Strings Equal
// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

#include <stdbool.h>

bool areAlmostEqual(char* s1, char* s2) {
    int first = -1;
    int second = -1;
    int count = 0;
    for (int i = 0; s1[i] != '\0'; i++) {
        if (s1[i] != s2[i]) {
            count++;
            if (count == 1) {
                first = i;
            } else if (count == 2) {
                second = i;
            } else {
                return false;
            }
        }
    }
    if (count == 0) return true;
    return count == 2 && s1[first] == s2[second] && s1[second] == s2[first];
}
