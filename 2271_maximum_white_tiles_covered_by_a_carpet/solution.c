// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

#include <stdlib.h>

static int cmp_pair(const void* a, const void* b) {
    int* const* pa = (int* const*)a;
    int* const* pb = (int* const*)b;
    return (*pa)[0] - (*pb)[0];
}

int maximumWhiteTiles(int** tiles, int tilesSize, int* tilesColSize, int carpetLen) {
    (void)tilesColSize;
    qsort(tiles, (size_t)tilesSize, sizeof(int*), cmp_pair);
    int* pref = (int*)malloc((size_t)(tilesSize + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < tilesSize; i++) {
        pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1);
    }
    int ans = 0;
    int j = 0;
    for (int i = 0; i < tilesSize; i++) {
        int end = tiles[i][0] + carpetLen - 1;
        while (j < tilesSize && tiles[j][0] <= end) j++;
        int cover = pref[j] - pref[i];
        if (j > 0 && tiles[j - 1][1] > end) {
            cover -= tiles[j - 1][1] - end;
        }
        if (cover > ans) ans = cover;
    }
    free(pref);
    return ans;
}
