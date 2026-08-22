// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

#include <stdlib.h>

int edgeScore(int* edges, int edgesSize) {
    long long* score = (long long*)calloc((size_t)edgesSize, sizeof(long long));
    for (int i = 0; i < edgesSize; i++) score[edges[i]] += i;
    int ans = 0;
    for (int i = 1; i < edgesSize; i++) if (score[i] > score[ans]) ans = i;
    free(score);
    return ans;
}
