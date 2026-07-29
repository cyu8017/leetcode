// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* destCity(char*** paths, int pathsSize, int* pathsColSize) {
    (void)pathsColSize;
    for (int i = 0; i < pathsSize; i++) {
        char* end = paths[i][1];
        bool isStart = false;
        for (int j = 0; j < pathsSize; j++)
            if (strcmp(paths[j][0], end) == 0) { isStart = true; break; }
        if (!isStart) {
            char* ans = (char*)malloc(strlen(end) + 1);
            strcpy(ans, end);
            return ans;
        }
    }
    return NULL;
}
