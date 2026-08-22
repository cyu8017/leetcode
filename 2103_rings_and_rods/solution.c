// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

#include <string.h>

int countPoints(char* rings) {
    int mask[10] = {0};
    int n = (int)strlen(rings);
    for (int i = 0; i < n; i += 2) {
        char c = rings[i];
        int r = rings[i + 1] - '0';
        int bit = c == 'R' ? 1 : (c == 'G' ? 2 : 4);
        mask[r] |= bit;
    }
    int ans = 0;
    for (int i = 0; i < 10; i++) if (mask[i] == 7) ans++;
    return ans;
}
