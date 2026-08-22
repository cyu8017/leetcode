// LeetCode 1247 - Minimum Swaps To Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

#include <string.h>

int minimumSwap(char* s1, char* s2) {
    int xy = 0, yx = 0;
    int n = (int)strlen(s1);
    for (int i = 0; i < n; i++) {
        if (s1[i] == 'x' && s2[i] == 'y') xy++;
        if (s1[i] == 'y' && s2[i] == 'x') yx++;
    }
    if ((xy + yx) % 2) return -1;
    return xy / 2 + yx / 2 + 2 * (xy % 2);
}
