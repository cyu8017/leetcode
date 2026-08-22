// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int* data;
    int size;
    int cap;
} IntList;

static void listAdd(IntList* list, int value) {
    if (list->size >= list->cap) {
        list->cap = list->cap ? list->cap * 2 : 4;
        list->data = (int*)realloc(list->data, (size_t)list->cap * sizeof(int));
    }
    list->data[list->size++] = value;
}

static int* topoOrder(IntList* graph, int* indeg, int n, int* outSize) {
    int* queue = (int*)malloc((size_t)n * sizeof(int));
    int qs = 0, qe = 0;
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0) queue[qe++] = i;
    }
    int* order = (int*)malloc((size_t)n * sizeof(int));
    int count = 0;
    while (qs < qe) {
        int u = queue[qs++];
        order[count++] = u;
        for (int i = 0; i < graph[u].size; i++) {
            int v = graph[u].data[i];
            if (--indeg[v] == 0) queue[qe++] = v;
        }
    }
    free(queue);
    if (count != n) {
        free(order);
        *outSize = 0;
        return NULL;
    }
    *outSize = n;
    return order;
}

int* sortItems(int n, int m, int* group, int** beforeItems, int* beforeItemsColSize, int* returnSize) {
    for (int i = 0; i < n; i++) {
        if (group[i] == -1) group[i] = m++;
    }
    IntList* itemGraph = (IntList*)calloc((size_t)n, sizeof(IntList));
    int* itemIndeg = (int*)calloc((size_t)n, sizeof(int));
    IntList* groupGraph = (IntList*)calloc((size_t)m, sizeof(IntList));
    int* groupIndeg = (int*)calloc((size_t)m, sizeof(int));
    char* groupEdge = (char*)calloc((size_t)m * (size_t)m, 1);
    for (int v = 0; v < n; v++) {
        for (int j = 0; j < beforeItemsColSize[v]; j++) {
            int u = beforeItems[v][j];
            listAdd(&itemGraph[u], v);
            itemIndeg[v]++;
            if (group[u] != group[v]) {
                int key = group[u] * m + group[v];
                if (!groupEdge[key]) {
                    groupEdge[key] = 1;
                    listAdd(&groupGraph[group[u]], group[v]);
                    groupIndeg[group[v]]++;
                }
            }
        }
    }
    int itemSize = 0;
    int groupSize = 0;
    int* itemOrder = topoOrder(itemGraph, itemIndeg, n, &itemSize);
    int* groupOrder = topoOrder(groupGraph, groupIndeg, m, &groupSize);
    if (!itemOrder || !groupOrder) {
        *returnSize = 0;
        return NULL;
    }
    IntList* buckets = (IntList*)calloc((size_t)m, sizeof(IntList));
    for (int i = 0; i < itemSize; i++) {
        int item = itemOrder[i];
        listAdd(&buckets[group[item]], item);
    }
    int total = 0;
    for (int i = 0; i < groupSize; i++) total += buckets[groupOrder[i]].size;
    int* ans = (int*)malloc((size_t)total * sizeof(int));
    int idx = 0;
    for (int i = 0; i < groupSize; i++) {
        IntList* bucket = &buckets[groupOrder[i]];
        for (int j = 0; j < bucket->size; j++) ans[idx++] = bucket->data[j];
    }
    for (int i = 0; i < n; i++) free(itemGraph[i].data);
    for (int i = 0; i < m; i++) {
        free(groupGraph[i].data);
        free(buckets[i].data);
    }
    free(itemGraph);
    free(groupGraph);
    free(buckets);
    free(itemIndeg);
    free(groupIndeg);
    free(groupEdge);
    free(itemOrder);
    free(groupOrder);
    *returnSize = total;
    return ans;
}
