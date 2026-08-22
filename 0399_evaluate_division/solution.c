// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NODES 64
#define MAX_NEIGHBORS 32

typedef struct {
    char name[8];
    int neighborCount;
    struct {
        int neighbor;
        double weight;
    } neighbors[MAX_NEIGHBORS];
} GraphNode;

typedef struct {
    GraphNode nodes[MAX_NODES];
    int nodeCount;
} Graph;

static int findNode(Graph* graph, const char* name, bool create) {
    for (int index = 0; index < graph->nodeCount; index++) {
        if (strcmp(graph->nodes[index].name, name) == 0) {
            return index;
        }
    }
    if (!create || graph->nodeCount == MAX_NODES) {
        return -1;
    }
    strcpy(graph->nodes[graph->nodeCount].name, name);
    graph->nodes[graph->nodeCount].neighborCount = 0;
    return graph->nodeCount++;
}

static void addEdge(Graph* graph, const char* from, const char* to, double weight) {
    int fromIndex = findNode(graph, from, true);
    int toIndex = findNode(graph, to, true);
    GraphNode* node = &graph->nodes[fromIndex];
    node->neighbors[node->neighborCount].neighbor = toIndex;
    node->neighbors[node->neighborCount].weight = weight;
    node->neighborCount += 1;
}

static double dfs(Graph* graph, int start, int end, bool* visited) {
    if (start < 0 || end < 0) {
        return -1.0;
    }
    if (start == end) {
        return 1.0;
    }
    visited[start] = true;
    GraphNode* node = &graph->nodes[start];
    for (int index = 0; index < node->neighborCount; index++) {
        int neighbor = node->neighbors[index].neighbor;
        if (visited[neighbor]) {
            continue;
        }
        double result = dfs(graph, neighbor, end, visited);
        if (result >= 0.0) {
            return node->neighbors[index].weight * result;
        }
    }
    return -1.0;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* calcEquation(
    char*** equations,
    int equationsSize,
    int* equationsColSize,
    double* values,
    int valuesSize,
    char*** queries,
    int queriesSize,
    int* queriesColSize,
    int* returnSize
) {
    (void)equationsColSize;
    (void)valuesSize;
    (void)queriesColSize;

    Graph graph = {0};
    for (int index = 0; index < equationsSize; index++) {
        addEdge(&graph, equations[index][0], equations[index][1], values[index]);
        addEdge(&graph, equations[index][1], equations[index][0], 1.0 / values[index]);
    }

    *returnSize = queriesSize;
    double* answers = (double*)malloc((size_t)queriesSize * sizeof(double));
    for (int index = 0; index < queriesSize; index++) {
        int start = findNode(&graph, queries[index][0], false);
        int end = findNode(&graph, queries[index][1], false);
        bool visited[MAX_NODES] = {false};
        answers[index] = dfs(&graph, start, end, visited);
    }

    return answers;
}
