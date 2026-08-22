// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool sequenceReconstruction(int* nums, int numsSize, int** sequences, int sequencesSize, int* sequencesColSize) {
    int* indegree = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    int** graph = (int**)calloc((size_t)numsSize + 1, sizeof(int*));
    int* graphSize = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    int* graphCap = (int*)calloc((size_t)numsSize + 1, sizeof(int));
    char* edgeSeen = (char*)calloc((size_t)(numsSize + 1) * (numsSize + 1), sizeof(char));

    for (int s = 0; s < sequencesSize; s++) {
        for (int index = 0; index < sequencesColSize[s] - 1; index++) {
            int left = sequences[s][index];
            int right = sequences[s][index + 1];
            int edgeKey = left * (numsSize + 1) + right;
            if (edgeSeen[edgeKey]) {
                continue;
            }
            edgeSeen[edgeKey] = 1;
            if (graphSize[left] == graphCap[left]) {
                graphCap[left] = graphCap[left] == 0 ? 4 : graphCap[left] * 2;
                graph[left] = (int*)realloc(graph[left], (size_t)graphCap[left] * sizeof(int));
            }
            graph[left][graphSize[left]++] = right;
            indegree[right]++;
        }
    }

    int* queue = (int*)malloc((size_t)numsSize * sizeof(int));
    int head = 0;
    int tail = 0;
    for (int i = 0; i < numsSize; i++) {
        if (indegree[nums[i]] == 0) {
            queue[tail++] = nums[i];
        }
    }

    int* order = (int*)malloc((size_t)numsSize * sizeof(int));
    int orderSize = 0;
    while (head < tail) {
        if (tail - head > 1) {
            free(indegree);
            for (int i = 0; i <= numsSize; i++) {
                free(graph[i]);
            }
            free(graph);
            free(graphSize);
            free(graphCap);
            free(edgeSeen);
            free(queue);
            free(order);
            return false;
        }
        int node = queue[head++];
        order[orderSize++] = node;
        for (int i = 0; i < graphSize[node]; i++) {
            int neighbor = graph[node][i];
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                queue[tail++] = neighbor;
            }
        }
    }

    bool ok = orderSize == numsSize;
    if (ok) {
        for (int i = 0; i < numsSize; i++) {
            if (order[i] != nums[i]) {
                ok = false;
                break;
            }
        }
    }

    free(indegree);
    for (int i = 0; i <= numsSize; i++) {
        free(graph[i]);
    }
    free(graph);
    free(graphSize);
    free(graphCap);
    free(edgeSeen);
    free(queue);
    free(order);
    return ok;
}
