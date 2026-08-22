// LeetCode 3279 - Maximum Total Area Occupied by Pistons
// https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

#include <stdlib.h>
#include <string.h>

long long maxArea(int height, int* positions, int positionsSize, char* directions) {
    int n = positionsSize;
    int* pos = (int*)malloc((size_t)n * sizeof(int));
    memcpy(pos, positions, (size_t)n * sizeof(int));
    char* dir = (char*)malloc((size_t)n + 1);
    memcpy(dir, directions, (size_t)n + 1);
    long long best = 0;
    for (int t = 0; t <= 2 * height; t++) {
        long long sum = 0;
        for (int i = 0; i < n; i++) sum += pos[i];
        if (sum > best) best = sum;
        for (int i = 0; i < n; i++) {
            if (dir[i] == 'U') {
                if (pos[i] == height) { dir[i] = 'D'; pos[i]--; }
                else pos[i]++;
            } else {
                if (pos[i] == 0) { dir[i] = 'U'; pos[i]++; }
                else pos[i]--;
            }
        }
    }
    free(pos); free(dir);
    return best;
}
