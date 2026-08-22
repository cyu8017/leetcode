// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define EQ_HASH 10007

typedef struct EqNode {
    char* name;
    char* parent;
    double weight;
    struct EqNode* next;
} EqNode;

typedef struct {
    EqNode* tab[EQ_HASH];
} UF;

static unsigned hstr(const char* s) {
    unsigned h = 2166136261u;
    while (*s) { h ^= (unsigned char)(*s++); h *= 16777619u; }
    return h % EQ_HASH;
}

static EqNode* get_node(UF* uf, char* x, bool create) {
    unsigned h = hstr(x);
    for (EqNode* p = uf->tab[h]; p; p = p->next) {
        if (strcmp(p->name, x) == 0) return p;
    }
    if (!create) return NULL;
    EqNode* n = (EqNode*)malloc(sizeof(EqNode));
    n->name = x;
    n->parent = x;
    n->weight = 1.0;
    n->next = uf->tab[h];
    uf->tab[h] = n;
    return n;
}

static EqNode* find_node(UF* uf, char* x) {
    EqNode* n = get_node(uf, x, true);
    if (strcmp(n->parent, n->name) != 0) {
        EqNode* p = find_node(uf, n->parent);
        // weight[x] *= weight[old_parent]; need old parent node
        EqNode* oldp = get_node(uf, n->parent, false);
        n->weight *= oldp->weight;
        n->parent = p->name;
        return p;
    }
    return n;
}

bool checkContradictions(char*** equations, int equationsSize, int* equationsColSize, double* values, int valuesSize) {
    (void)equationsColSize; (void)valuesSize;
    UF uf;
    memset(&uf, 0, sizeof(uf));
    for (int i = 0; i < equationsSize; i++) {
        char* a = equations[i][0];
        char* b = equations[i][1];
        EqNode* ra = find_node(&uf, a);
        EqNode* rb = find_node(&uf, b);
        EqNode* na = get_node(&uf, a, false);
        EqNode* nb = get_node(&uf, b, false);
        if (strcmp(ra->name, rb->name) == 0) {
            if (fabs(na->weight / nb->weight - values[i]) > 1e-5) {
                // free and return
                for (int h = 0; h < EQ_HASH; h++) {
                    EqNode* p = uf.tab[h];
                    while (p) { EqNode* nx = p->next; free(p); p = nx; }
                }
                return true;
            }
        } else {
            // parent[ra] = rb; weight[ra] = values[i] * weight[b] / weight[a]
            ra->parent = rb->name;
            ra->weight = values[i] * nb->weight / na->weight;
        }
    }
    for (int h = 0; h < EQ_HASH; h++) {
        EqNode* p = uf.tab[h];
        while (p) { EqNode* nx = p->next; free(p); p = nx; }
    }
    return false;
}
