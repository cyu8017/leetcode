// LeetCode 1079 - Letter Tile Possibilities
// https://leetcode.com/problems/letter-tile-possibilities/

#include <string.h>

static int dfs(int* count) {
    int total = 0;
    for (int i = 0; i < 26; i++) {
        if (count[i] == 0) {
            continue;
        }
        count[i]--;
        total += 1 + dfs(count);
        count[i]++;
    }
    return total;
}

int numTilePossibilities(char* tiles) {
    int count[26] = {0};
    for (char* p = tiles; *p; p++) {
        count[*p - 'A']++;
    }
    return dfs(count);
}
