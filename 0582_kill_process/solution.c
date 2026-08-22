// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* killProcess(int* pid, int pidSize, int* ppid, int ppidSize, int kill, int* returnSize) {
    (void)ppidSize;
    int maxId = 0;
    for (int i = 0; i < pidSize; i++) {
        if (pid[i] > maxId) {
            maxId = pid[i];
        }
        if (ppid[i] > maxId) {
            maxId = ppid[i];
        }
    }

    int* childCount = (int*)calloc((size_t)maxId + 1, sizeof(int));
    for (int i = 0; i < pidSize; i++) {
        childCount[ppid[i]]++;
    }
    int** children = (int**)calloc((size_t)maxId + 1, sizeof(int*));
    int* filled = (int*)calloc((size_t)maxId + 1, sizeof(int));
    for (int i = 0; i <= maxId; i++) {
        if (childCount[i] > 0) {
            children[i] = (int*)malloc((size_t)childCount[i] * sizeof(int));
        }
    }
    for (int i = 0; i < pidSize; i++) {
        int parent = ppid[i];
        children[parent][filled[parent]++] = pid[i];
    }

    int* result = (int*)malloc((size_t)pidSize * sizeof(int));
    int* queue = (int*)malloc((size_t)pidSize * sizeof(int));
    int head = 0;
    int tail = 0;
    int count = 0;
    queue[tail++] = kill;
    while (head < tail) {
        int process = queue[head++];
        result[count++] = process;
        for (int i = 0; i < childCount[process]; i++) {
            queue[tail++] = children[process][i];
        }
    }

    for (int i = 0; i <= maxId; i++) {
        free(children[i]);
    }
    free(children);
    free(childCount);
    free(filled);
    free(queue);
    *returnSize = count;
    return result;
}
