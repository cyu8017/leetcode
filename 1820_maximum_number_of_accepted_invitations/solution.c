// LeetCode 1820 - Maximum Number of Accepted Invitations
// https://leetcode.com/problems/maximum-number-of-accepted-invitations/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool dfsInvite(int boy, int** grid, int girls, int* matchGirl, bool* seen) {
    for (int girl = 0; girl < girls; girl++) {
        if (grid[boy][girl] && !seen[girl]) {
            seen[girl] = true;
            if (matchGirl[girl] == -1 || dfsInvite(matchGirl[girl], grid, girls, matchGirl, seen)) {
                matchGirl[girl] = boy;
                return true;
            }
        }
    }
    return false;
}

int maximumInvitations(int** grid, int gridSize, int* gridColSize) {
    int boys = gridSize;
    int girls = gridColSize[0];
    int* matchGirl = (int*)malloc((size_t)girls * sizeof(int));
    for (int i = 0; i < girls; i++) matchGirl[i] = -1;

    int ans = 0;
    bool* seen = (bool*)malloc((size_t)girls * sizeof(bool));
    for (int boy = 0; boy < boys; boy++) {
        memset(seen, 0, (size_t)girls * sizeof(bool));
        if (dfsInvite(boy, grid, girls, matchGirl, seen)) ans++;
    }
    free(seen);
    free(matchGirl);
    return ans;
}
