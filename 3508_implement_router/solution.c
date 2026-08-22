// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int used;
} VisEntry;

typedef struct {
    int lim;
    VisEntry* vis;
    int visCap;
    int* q; /* triples flat */
    int qHead, qTail, qCap;
    int* idx; /* dest -> start index in d lists - use parallel arrays */
    int** d;
    int* dsz;
    int* dcap;
    int* dIdx; /* dest -> consumed count */
    int maxDest;
} Router;

static long long fkey(int a, int b, int c) {
    return ((long long)a << 46) | ((long long)b << 29) | (long long)c;
}

static int visFind(Router* obj, long long key, int create) {
    unsigned h = (unsigned)(key % (unsigned)obj->visCap);
    for (int i = 0; i < obj->visCap; i++) {
        int j = (h + i) % obj->visCap;
        if (!obj->vis[j].used) {
            if (!create) return -1;
            obj->vis[j].used = 1;
            obj->vis[j].key = key;
            return j;
        }
        if (obj->vis[j].key == key) return j;
    }
    return -1;
}

Router* routerCreate(int memoryLimit) {
    Router* obj = (Router*)calloc(1, sizeof(Router));
    obj->lim = memoryLimit;
    obj->visCap = memoryLimit * 4 + 16;
    obj->vis = (VisEntry*)calloc((size_t)obj->visCap, sizeof(VisEntry));
    obj->qCap = memoryLimit + 8;
    obj->q = (int*)malloc((size_t)obj->qCap * 3 * sizeof(int));
    obj->maxDest = 200005;
    obj->d = (int**)calloc((size_t)obj->maxDest, sizeof(int*));
    obj->dsz = (int*)calloc((size_t)obj->maxDest, sizeof(int));
    obj->dcap = (int*)calloc((size_t)obj->maxDest, sizeof(int));
    obj->dIdx = (int*)calloc((size_t)obj->maxDest, sizeof(int));
    return obj;
}

static int* routerForwardPacket(Router* obj, int* returnSize);

bool routerAddPacket(Router* obj, int source, int destination, int timestamp) {
    long long x = fkey(source, destination, timestamp);
    if (visFind(obj, x, 0) >= 0) return false;
    visFind(obj, x, 1);
    if (obj->qTail - obj->qHead >= obj->lim) {
        int rs;
        int* tmp = routerForwardPacket(obj, &rs);
        free(tmp);
    }
    if (obj->qTail >= obj->qCap) {
        /* compact */
        int len = obj->qTail - obj->qHead;
        memmove(obj->q, obj->q + obj->qHead * 3, (size_t)len * 3 * sizeof(int));
        obj->qTail = len; obj->qHead = 0;
    }
    int p = obj->qTail++;
    obj->q[p * 3] = source; obj->q[p * 3 + 1] = destination; obj->q[p * 3 + 2] = timestamp;
    int d = destination;
    if (obj->dsz[d] == obj->dcap[d]) {
        obj->dcap[d] = obj->dcap[d] ? obj->dcap[d] * 2 : 4;
        obj->d[d] = (int*)realloc(obj->d[d], (size_t)obj->dcap[d] * sizeof(int));
    }
    obj->d[d][obj->dsz[d]++] = timestamp;
    return true;
}

int* routerForwardPacket(Router* obj, int* returnSize) {
    if (obj->qHead >= obj->qTail) {
        *returnSize = 0;
        return NULL;
    }
    int s = obj->q[obj->qHead * 3];
    int d = obj->q[obj->qHead * 3 + 1];
    int t = obj->q[obj->qHead * 3 + 2];
    obj->qHead++;
    long long x = fkey(s, d, t);
    int vi = visFind(obj, x, 0);
    if (vi >= 0) obj->vis[vi].used = 0;
    obj->dIdx[d]++;
    int* out = (int*)malloc(3 * sizeof(int));
    out[0] = s; out[1] = d; out[2] = t;
    *returnSize = 3;
    return out;
}

static int lowerBound(int* a, int lo, int hi, int x) {
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

int routerGetCount(Router* obj, int destination, int startTime, int endTime) {
    int* ls = obj->d[destination];
    int n = obj->dsz[destination];
    int k = obj->dIdx[destination];
    int i = lowerBound(ls, k, n, startTime);
    int j = lowerBound(ls, k, n, endTime + 1);
    return j - i;
}

void routerFree(Router* obj) {
    free(obj->vis); free(obj->q);
    for (int i = 0; i < obj->maxDest; i++) free(obj->d[i]);
    free(obj->d); free(obj->dsz); free(obj->dcap); free(obj->dIdx);
    free(obj);
}
