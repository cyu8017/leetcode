// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

#include <stdlib.h>

int* longestObstacleCourseAtEachPosition(int* obstacles, int obstaclesSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)obstaclesSize * sizeof(int));
    int* tails = (int*)malloc((size_t)obstaclesSize * sizeof(int));
    int len = 0;
    for (int i = 0; i < obstaclesSize; i++) {
        int x = obstacles[i];
        int lo = 0, hi = len;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (tails[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        if (lo == len) tails[len++] = x;
        else tails[lo] = x;
        ans[i] = lo + 1;
    }
    free(tails);
    *returnSize = obstaclesSize;
    return ans;
}
