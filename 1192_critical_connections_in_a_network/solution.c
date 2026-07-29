// LeetCode 1192 - Critical Connections in a Network
// https://leetcode.com/problems/critical-connections-in-a-network/

#include <stdlib.h>
#include <string.h>

typedef struct Edge {
    int to;
    struct Edge* next;
} Edge;

typedef struct {
    Edge** heads;
    int* disc;
    int* low;
    int time;
    int** result;
    int* colSizes;
    int count;
    int capacity;
} BridgeContext;

static void addEdge(BridgeContext* ctx, int u, int v) {
    Edge* e1 = (Edge*)malloc(sizeof(Edge));
    e1->to = v;
    e1->next = ctx->heads[u];
    ctx->heads[u] = e1;
    Edge* e2 = (Edge*)malloc(sizeof(Edge));
    e2->to = u;
    e2->next = ctx->heads[v];
    ctx->heads[v] = e2;
}

static void dfs(BridgeContext* ctx, int node, int parent) {
    ctx->disc[node] = ctx->low[node] = ctx->time++;
    for (Edge* e = ctx->heads[node]; e; e = e->next) {
        int nxt = e->to;
        if (nxt == parent) continue;
        if (ctx->disc[nxt] == -1) {
            dfs(ctx, nxt, node);
            if (ctx->low[nxt] < ctx->low[node]) ctx->low[node] = ctx->low[nxt];
            if (ctx->low[nxt] > ctx->disc[node]) {
                if (ctx->count >= ctx->capacity) {
                    ctx->capacity *= 2;
                    ctx->result = (int**)realloc(ctx->result, (size_t)ctx->capacity * sizeof(int*));
                    ctx->colSizes = (int*)realloc(ctx->colSizes, (size_t)ctx->capacity * sizeof(int));
                }
                ctx->result[ctx->count] = (int*)malloc(2 * sizeof(int));
                ctx->result[ctx->count][0] = node < nxt ? node : nxt;
                ctx->result[ctx->count][1] = node < nxt ? nxt : node;
                ctx->colSizes[ctx->count] = 2;
                ctx->count++;
            }
        } else if (ctx->disc[nxt] < ctx->low[node]) {
            ctx->low[node] = ctx->disc[nxt];
        }
    }
}

int** criticalConnections(int n, int** connections, int connectionsSize, int* connectionsColSize, int* returnSize, int** returnColumnSizes) {
    (void)connectionsColSize;
    BridgeContext ctx;
    ctx.heads = (Edge**)calloc((size_t)n, sizeof(Edge*));
    ctx.disc = (int*)malloc((size_t)n * sizeof(int));
    ctx.low = (int*)malloc((size_t)n * sizeof(int));
    memset(ctx.disc, -1, (size_t)n * sizeof(int));
    ctx.time = 0;
    ctx.capacity = 16;
    ctx.count = 0;
    ctx.result = (int**)malloc((size_t)ctx.capacity * sizeof(int*));
    ctx.colSizes = (int*)malloc((size_t)ctx.capacity * sizeof(int));
    for (int i = 0; i < connectionsSize; i++) addEdge(&ctx, connections[i][0], connections[i][1]);
    dfs(&ctx, 0, -1);
    for (int i = 0; i < n; i++) {
        Edge* e = ctx.heads[i];
        while (e) {
            Edge* next = e->next;
            free(e);
            e = next;
        }
    }
    free(ctx.heads);
    free(ctx.disc);
    free(ctx.low);
    *returnSize = ctx.count;
    *returnColumnSizes = (int*)realloc(ctx.colSizes, (size_t)ctx.count * sizeof(int));
    ctx.result = (int**)realloc(ctx.result, (size_t)ctx.count * sizeof(int*));
    return ctx.result;
}
