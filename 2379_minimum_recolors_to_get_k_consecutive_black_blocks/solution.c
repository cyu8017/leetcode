// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

#include <string.h>

int minimumRecolors(char* blocks, int k) {
    int white = 0, n = (int)strlen(blocks);
    for (int i = 0; i < k; i++) if (blocks[i] == 'W') white++;
    int ans = white;
    for (int i = k; i < n; i++) {
        if (blocks[i] == 'W') white++;
        if (blocks[i - k] == 'W') white--;
        if (white < ans) ans = white;
    }
    return ans;
}
