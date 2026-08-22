// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int encode(const int* arr, int n) {
    int key = 0;
    for (int i = 0; i < n; i++) key = key * 8 + arr[i];
    return key;
}

int sortArray(int* nums, int numsSize, int* pre, int preSize) {
    int n = numsSize;
    int target = 0;
    for (int i = 0; i < n; i++) target = target * 8 + i;

    int start = encode(nums, n);
    if (start == target) return 0;

    int lengths[64];
    int lengthCount = 0;
    for (int i = 0; i < preSize; i++) {
        int x = pre[i];
        if (x < 2 || x > n) continue;
        bool seen = false;
        for (int j = 0; j < lengthCount; j++) {
            if (lengths[j] == x) { seen = true; break; }
        }
        if (!seen) lengths[lengthCount++] = x;
    }

    int cap = 1 << 16;
    int* visitedKeys = (int*)malloc((size_t)cap * sizeof(int));
    char* visitedUsed = (char*)calloc((size_t)cap, 1);
    int* queueStates = (int*)malloc((size_t)cap * n * sizeof(int));
    int* queueDists = (int*)malloc((size_t)cap * sizeof(int));
    if (!visitedKeys || !visitedUsed || !queueStates || !queueDists) {
        free(visitedKeys); free(visitedUsed); free(queueStates); free(queueDists);
        return -1;
    }

    int visitedCount = 0;
    visitedKeys[visitedCount] = start;
    visitedUsed[visitedCount++] = 1;

    int qh = 0, qt = 0;
    memcpy(queueStates, nums, (size_t)n * sizeof(int));
    queueDists[qt++] = 0;

    while (qh < qt) {
        int* cur = queueStates + qh * n;
        int dist = queueDists[qh++];
        int nd = dist + 1;

        for (int li = 0; li < lengthCount; li++) {
            int x = lengths[li];
            int nxt[16];
            memcpy(nxt, cur, (size_t)n * sizeof(int));
            for (int l = 0, r = x - 1; l < r; l++, r--) {
                int tmp = nxt[l];
                nxt[l] = nxt[r];
                nxt[r] = tmp;
            }
            int key = encode(nxt, n);
            if (key == target) {
                free(visitedKeys); free(visitedUsed); free(queueStates); free(queueDists);
                return nd;
            }
            bool seen = false;
            for (int i = 0; i < visitedCount; i++) {
                if (visitedKeys[i] == key) { seen = true; break; }
            }
            if (!seen) {
                if (visitedCount == cap || qt == cap) {
                    free(visitedKeys); free(visitedUsed); free(queueStates); free(queueDists);
                    return -1;
                }
                visitedKeys[visitedCount++] = key;
                memcpy(queueStates + qt * n, nxt, (size_t)n * sizeof(int));
                queueDists[qt++] = nd;
            }
        }
    }

    free(visitedKeys); free(visitedUsed); free(queueStates); free(queueDists);
    return -1;
}
