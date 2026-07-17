// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int versionCount;
    int* weights;
    int** versions;
} DistanceLimitedPathsExist;

typedef struct {
    int w;
    int u;
    int v;
} Edge;

static int compareEdges(const void* a, const void* b) {
    const Edge* ea = (const Edge*)a;
    const Edge* eb = (const Edge*)b;
    if (ea->w != eb->w) return ea->w < eb->w ? -1 : 1;
    if (ea->u != eb->u) return ea->u < eb->u ? -1 : 1;
    if (ea->v != eb->v) return ea->v < eb->v ? -1 : 1;
    return 0;
}

static int findCompress(int* parent, int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

DistanceLimitedPathsExist* distanceLimitedPathsExistCreate(int n, int** edgeList, int edgeListSize,
                                                           int* edgeListColSize) {
    DistanceLimitedPathsExist* obj =
        (DistanceLimitedPathsExist*)malloc(sizeof(DistanceLimitedPathsExist));
    obj->n = n;
    obj->versionCount = 0;
    obj->weights = (int*)malloc(edgeListSize * sizeof(int));
    obj->versions = (int**)malloc(edgeListSize * sizeof(int*));
    Edge* edges = (Edge*)malloc(edgeListSize * sizeof(Edge));
    for (int i = 0; i < edgeListSize; i++) {
        edges[i].w = edgeList[i][2];
        edges[i].u = edgeList[i][0];
        edges[i].v = edgeList[i][1];
    }
    qsort(edges, edgeListSize, sizeof(Edge), compareEdges);
    int* parent = (int*)malloc(n * sizeof(int));
    int* size = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        parent[i] = i;
        size[i] = 1;
    }
    int i = 0;
    while (i < edgeListSize) {
        int weight = edges[i].w;
        while (i < edgeListSize && edges[i].w == weight) {
            int ra = findCompress(parent, edges[i].u);
            int rb = findCompress(parent, edges[i].v);
            if (ra != rb) {
                if (size[ra] < size[rb]) {
                    int tmp = ra;
                    ra = rb;
                    rb = tmp;
                }
                parent[rb] = ra;
                size[ra] += size[rb];
            }
            i++;
        }
        obj->weights[obj->versionCount] = weight;
        obj->versions[obj->versionCount] = (int*)malloc(n * sizeof(int));
        memcpy(obj->versions[obj->versionCount], parent, n * sizeof(int));
        obj->versionCount++;
    }
    free(edges);
    free(parent);
    free(size);
    return obj;
}

bool distanceLimitedPathsExistQuery(DistanceLimitedPathsExist* obj, int p, int q, int limit) {
    int lo = 0;
    int hi = obj->versionCount;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (obj->weights[mid] < limit) lo = mid + 1;
        else hi = mid;
    }
    int idx = lo - 1;
    if (idx < 0) return p == q;
    const int* parent = obj->versions[idx];
    int rp = p;
    while (parent[rp] != rp) rp = parent[rp];
    int rq = q;
    while (parent[rq] != rq) rq = parent[rq];
    return rp == rq;
}

void distanceLimitedPathsExistFree(DistanceLimitedPathsExist* obj) {
    for (int i = 0; i < obj->versionCount; i++) {
        free(obj->versions[i]);
    }
    free(obj->versions);
    free(obj->weights);
    free(obj);
}
