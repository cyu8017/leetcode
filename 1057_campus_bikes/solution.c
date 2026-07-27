// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int dist;
    int worker;
    int bike;
} Triple;

static int cmpTriple(const void* a, const void* b) {
    const Triple* ta = (const Triple*)a;
    const Triple* tb = (const Triple*)b;
    if (ta->dist != tb->dist) {
        return ta->dist - tb->dist;
    }
    if (ta->worker != tb->worker) {
        return ta->worker - tb->worker;
    }
    return ta->bike - tb->bike;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignBikes(int** workers, int workersSize, int* workersColSize, int** bikes, int bikesSize,
                 int* bikesColSize, int* returnSize) {
    (void)workersColSize;
    (void)bikesColSize;
    int total = workersSize * bikesSize;
    Triple* triples = (Triple*)malloc((size_t)total * sizeof(Triple));
    int t = 0;
    for (int w = 0; w < workersSize; w++) {
        for (int b = 0; b < bikesSize; b++) {
            triples[t].dist = abs(workers[w][0] - bikes[b][0]) + abs(workers[w][1] - bikes[b][1]);
            triples[t].worker = w;
            triples[t].bike = b;
            t++;
        }
    }
    qsort(triples, (size_t)total, sizeof(Triple), cmpTriple);
    int* ans = (int*)malloc((size_t)workersSize * sizeof(int));
    for (int i = 0; i < workersSize; i++) {
        ans[i] = -1;
    }
    bool* usedBikes = (bool*)calloc((size_t)bikesSize, sizeof(bool));
    int assigned = 0;
    for (int i = 0; i < total && assigned < workersSize; i++) {
        int w = triples[i].worker;
        int b = triples[i].bike;
        if (ans[w] == -1 && !usedBikes[b]) {
            ans[w] = b;
            usedBikes[b] = true;
            assigned++;
        }
    }
    free(triples);
    free(usedBikes);
    *returnSize = workersSize;
    return ans;
}
