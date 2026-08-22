// LeetCode 3841 - Palindromic Path Queries in a Tree
// https://leetcode.com/problems/palindromic-path-queries-in-a-tree/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdio.h>

static void bit_upd(int* bit, int n, int index, int value) {
    for (index++; index <= n; index += index & -index) bit[index] ^= value;
}
static int bit_pre(int* bit, int index) {
    int result = 0;
    for (; index > 0; index -= index & -index) result ^= bit[index];
    return result;
}

bool* palindromicPathQueries(int n, int** edges, int edgesSize, int* edgesColSize, char* s, char** queries, int queriesSize, int* returnSize) {
    (void)edgesColSize;
    int** graph = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (deg[u] == cap[u]) { cap[u] = cap[u] ? cap[u]*2 : 4; graph[u] = (int*)realloc(graph[u], (size_t)cap[u]*sizeof(int)); }
        graph[u][deg[u]++] = v;
        if (deg[v] == cap[v]) { cap[v] = cap[v] ? cap[v]*2 : 4; graph[v] = (int*)realloc(graph[v], (size_t)cap[v]*sizeof(int)); }
        graph[v][deg[v]++] = u;
    }
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    int* depth = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = -2;
    parent[0] = -1;
    int* order = (int*)malloc((size_t)n * sizeof(int));
    int osz = 0;
    order[osz++] = 0;
    for (int i = 0; i < osz; i++) {
        int u = order[i];
        for (int j = 0; j < deg[u]; j++) {
            int v = graph[u][j];
            if (parent[v] == -2) { parent[v] = u; depth[v] = depth[u] + 1; order[osz++] = v; }
        }
    }
    int* size = (int*)malloc((size_t)n * sizeof(int));
    int* heavy = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) heavy[i] = -1;
    for (int i = n - 1; i >= 0; i--) {
        int u = order[i];
        size[u] = 1;
        for (int j = 0; j < deg[u]; j++) {
            int v = graph[u][j];
            if (parent[v] == u) {
                size[u] += size[v];
                if (heavy[u] == -1 || size[v] > size[heavy[u]]) heavy[u] = v;
            }
        }
    }
    int* head = (int*)malloc((size_t)n * sizeof(int));
    int* position = (int*)malloc((size_t)n * sizeof(int));
    int* stack_node = (int*)malloc((size_t)n * 2 * sizeof(int));
    int* stack_head = (int*)malloc((size_t)n * 2 * sizeof(int));
    int st = 0;
    stack_node[st] = 0; stack_head[st] = 0; st++;
    int nextPosition = 0;
    while (st > 0) {
        st--;
        int cnode = stack_node[st], chead = stack_head[st];
        for (int u = cnode; u != -1; u = heavy[u]) {
            head[u] = chead;
            position[u] = nextPosition++;
            for (int j = 0; j < deg[u]; j++) {
                int v = graph[u][j];
                if (parent[v] == u && v != heavy[u]) {
                    stack_node[st] = v; stack_head[st] = v; st++;
                }
            }
        }
    }
    int* bit = (int*)calloc((size_t)n + 1, sizeof(int));
    char* current = (char*)malloc((size_t)n + 1);
    memcpy(current, s, (size_t)n);
    current[n] = '\0';
    for (int node = 0; node < n; node++) bit_upd(bit, n, position[node], 1 << (current[node] - 'a'));

    bool* answer = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    int asz = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        char buf[256];
        strncpy(buf, queries[qi], sizeof(buf) - 1);
        buf[sizeof(buf) - 1] = '\0';
        char* tok = strtok(buf, " ");
        char* t1 = strtok(NULL, " ");
        char* t2 = strtok(NULL, " ");
        int node = atoi(t1);
        if (strcmp(tok, "update") == 0) {
            char newCharacter = t2[0];
            int delta = (1 << (current[node] - 'a')) ^ (1 << (newCharacter - 'a'));
            bit_upd(bit, n, position[node], delta);
            current[node] = newCharacter;
            continue;
        }
        int other = atoi(t2);
        int u = node, v = other;
        int result = 0;
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) { int tmp = u; u = v; v = tmp; }
            result ^= bit_pre(bit, position[u] + 1) ^ bit_pre(bit, position[head[u]]);
            u = parent[head[u]];
        }
        if (position[u] > position[v]) { int tmp = u; u = v; v = tmp; }
        int mask = result ^ bit_pre(bit, position[v] + 1) ^ bit_pre(bit, position[u]);
        answer[asz++] = (mask & (mask - 1)) == 0;
    }
    for (int i = 0; i < n; i++) free(graph[i]);
    free(graph); free(deg); free(cap); free(parent); free(depth); free(order);
    free(size); free(heavy); free(head); free(position); free(stack_node); free(stack_head);
    free(bit); free(current);
    *returnSize = asz;
    return answer;
}
