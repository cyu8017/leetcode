// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isPathCrossing(char* path) {
    int n = (int)strlen(path);
    int* xs = (int*)malloc((n + 1) * sizeof(int));
    int* ys = (int*)malloc((n + 1) * sizeof(int));
    int sn = 1; xs[0] = 0; ys[0] = 0;
    int x = 0, y = 0;
    for (int i = 0; path[i]; i++) {
        if (path[i] == 'N') y++;
        else if (path[i] == 'S') y--;
        else if (path[i] == 'E') x++;
        else x--;
        for (int j = 0; j < sn; j++)
            if (xs[j] == x && ys[j] == y) { free(xs); free(ys); return true; }
        xs[sn] = x; ys[sn] = y; sn++;
    }
    free(xs); free(ys);
    return false;
}
