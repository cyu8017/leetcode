// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

#include <stdlib.h>
#include <string.h>

#define MAXC 64
#define MAXE 256

typedef struct { char name[16]; double amt; int used; } Node;
typedef struct { int from, to; double rate; } Edge;

static int find_or_add(Node* nodes, int* n, const char* s) {
    for (int i = 0; i < *n; i++) if (strcmp(nodes[i].name, s) == 0) return i;
    strcpy(nodes[*n].name, s); nodes[*n].amt = 0; nodes[*n].used = 1; return (*n)++;
}

static void bellman(Node* nodes, int nc, Edge* edges, int en, int start) {
    for (int i = 0; i < nc; i++) nodes[i].amt = 0;
    nodes[start].amt = 1.0;
    for (int it = 0; it < 100; it++) {
        int updated = 0;
        for (int e = 0; e < en; e++) {
            if (nodes[edges[e].from].amt == 0) continue;
            double nv = nodes[edges[e].from].amt * edges[e].rate;
            if (nv > nodes[edges[e].to].amt) { nodes[edges[e].to].amt = nv; updated = 1; }
        }
        if (!updated) break;
    }
}

double maxAmount(char* initialCurrency, char*** pairs1, int pairs1Size, int* pairs1ColSize, double* rates1, int rates1Size, char*** pairs2, int pairs2Size, int* pairs2ColSize, double* rates2, int rates2Size) {
    (void)pairs1ColSize; (void)pairs2ColSize; (void)rates1Size; (void)rates2Size;
    Node nodes[MAXC]; int nc = 0;
    int start = find_or_add(nodes, &nc, initialCurrency);
    Edge e1[MAXE]; int n1 = 0;
    for (int i = 0; i < pairs1Size; i++) {
        int a = find_or_add(nodes, &nc, pairs1[i][0]);
        int b = find_or_add(nodes, &nc, pairs1[i][1]);
        e1[n1++] = (Edge){a, b, rates1[i]};
        e1[n1++] = (Edge){b, a, 1.0 / rates1[i]};
    }
    Edge e2[MAXE]; int n2 = 0;
    for (int i = 0; i < pairs2Size; i++) {
        int a = find_or_add(nodes, &nc, pairs2[i][0]);
        int b = find_or_add(nodes, &nc, pairs2[i][1]);
        e2[n2++] = (Edge){a, b, rates2[i]};
        e2[n2++] = (Edge){b, a, 1.0 / rates2[i]};
    }
    Node day1[MAXC]; memcpy(day1, nodes, sizeof(nodes));
    bellman(day1, nc, e1, n1, start);
    double ans = 1.0;
    for (int c = 0; c < nc; c++) {
        if (day1[c].amt <= 0) continue;
        Node dist[MAXC];
        for (int i = 0; i < nc; i++) { strcpy(dist[i].name, nodes[i].name); dist[i].amt = 0; }
        dist[c].amt = day1[c].amt;
        for (int it = 0; it < nc; it++) {
            int updated = 0;
            for (int e = 0; e < n2; e++) {
                if (dist[e2[e].from].amt == 0) continue;
                double nv = dist[e2[e].from].amt * e2[e].rate;
                if (nv > dist[e2[e].to].amt) { dist[e2[e].to].amt = nv; updated = 1; }
            }
            if (!updated) break;
        }
        if (dist[start].amt > ans) ans = dist[start].amt;
    }
    return ans;
}
