// LeetCode 0815 - Bus Routes
// https://leetcode.com/problems/bus-routes/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int stop, buses; } QNode;
typedef struct { int stop, bus; } Edge;

static int cmp_edge(const void* a, const void* b) {
    const Edge* x = a; const Edge* y = b;
    if (x->stop != y->stop) return x->stop - y->stop;
    return x->bus - y->bus;
}

int numBusesToDestination(int** routes, int routesSize, int* routesColSize, int source, int target) {
    if (source == target) return 0;
    int total = 0;
    for (int i = 0; i < routesSize; i++) total += routesColSize[i];
    Edge* edges = (Edge*)malloc((size_t)total * sizeof(Edge));
    int ne = 0;
    for (int bus = 0; bus < routesSize; bus++)
        for (int j = 0; j < routesColSize[bus]; j++)
            edges[ne++] = (Edge){routes[bus][j], bus};
    qsort(edges, (size_t)ne, sizeof(Edge), cmp_edge);

    QNode* q = (QNode*)malloc((size_t)(ne + 1) * sizeof(QNode));
    int qh = 0, qt = 0;
    bool* seenStops = (bool*)calloc(1000001, sizeof(bool));
    bool* seenBuses = (bool*)calloc((size_t)routesSize, sizeof(bool));
    q[qt++] = (QNode){source, 0};
    seenStops[source] = true;

    while (qh < qt) {
        QNode cur = q[qh++];
        int lo = 0, hi = ne;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (edges[mid].stop < cur.stop) lo = mid + 1;
            else hi = mid;
        }
        for (int i = lo; i < ne && edges[i].stop == cur.stop; i++) {
            int bus = edges[i].bus;
            if (seenBuses[bus]) continue;
            seenBuses[bus] = true;
            for (int j = 0; j < routesColSize[bus]; j++) {
                int nxt = routes[bus][j];
                if (nxt == target) {
                    free(edges); free(q); free(seenStops); free(seenBuses);
                    return cur.buses + 1;
                }
                if (!seenStops[nxt]) {
                    seenStops[nxt] = true;
                    q[qt++] = (QNode){nxt, cur.buses + 1};
                }
            }
        }
    }
    free(edges); free(q); free(seenStops); free(seenBuses);
    return -1;
}
