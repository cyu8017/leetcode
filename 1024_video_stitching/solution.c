// LeetCode 1024 - Video Stitching
// https://leetcode.com/problems/video-stitching/

#include <stdlib.h>
#include <string.h>

int videoStitching(int** clips, int clipsSize, int* clipsColSize, int time) {
    (void)clipsColSize;
    int* furthest = (int*)calloc((size_t)(time + 1), sizeof(int));
    for (int i = 0; i < clipsSize; i++) {
        int start = clips[i][0], end = clips[i][1];
        if (start <= time && end > furthest[start]) furthest[start] = end;
    }
    int ans = 0, reach = 0, nextReach = 0;
    for (int i = 0; i < time; i++) {
        if (furthest[i] > nextReach) nextReach = furthest[i];
        if (i == reach) {
            if (nextReach <= i) {
                free(furthest);
                return -1;
            }
            ans++;
            reach = nextReach;
        }
    }
    free(furthest);
    return ans;
}
