// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct { int key, parent, size; bool used; } Node;

static unsigned hush(int x) { return (unsigned)x * 2654435761u; }

static Node* findSlot(Node* t, int cap, int key, int create) {
    unsigned h = hush(key) % (unsigned)cap;
    for (int i = 0; i < cap; i++) {
        unsigned idx = (h + i) % (unsigned)cap;
        if (!t[idx].used) {
            if (!create) return NULL;
            t[idx].used = true; t[idx].key = key; t[idx].parent = key; t[idx].size = 0;
            return &t[idx];
        }
        if (t[idx].key == key) return &t[idx];
    }
    return NULL;
}

static int findP(Node* t, int cap, int x) {
    Node* n = findSlot(t, cap, x, 0);
    if (n->parent != x) n->parent = findP(t, cap, n->parent);
    return n->parent;
}

static void unite(Node* t, int cap, int a, int b) {
    int ra = findP(t, cap, a), rb = findP(t, cap, b);
    if (ra == rb) return;
    Node *A = findSlot(t, cap, ra, 0), *B = findSlot(t, cap, rb, 0);
    if (A->size < B->size) { int tmp = ra; ra = rb; rb = tmp; A = findSlot(t, cap, ra, 0); B = findSlot(t, cap, rb, 0); }
    B->parent = ra;
    A->size += B->size;
}

int* groupStrings(char** words, int wordsSize, int* returnSize) {
    int cap = 1 << 15;
    Node* t = (Node*)calloc((size_t)cap, sizeof(Node));
    for (int i = 0; i < wordsSize; i++) {
        int m = 0;
        for (char* p = words[i]; *p; p++) m |= 1 << (*p - 'a');
        Node* n = findSlot(t, cap, m, 1);
        n->size++;
    }
    // collect keys
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int kn = 0;
    for (int i = 0; i < cap; i++) if (t[i].used) keys[kn++] = t[i].key;
    for (int ki = 0; ki < kn; ki++) {
        int m = keys[ki];
        for (int b = 0; b < 26; b++) {
            if (m & (1 << b)) {
                int nm = m ^ (1 << b);
                if (findSlot(t, cap, nm, 0)) unite(t, cap, m, nm);
                for (int a = 0; a < 26; a++) {
                    if ((nm & (1 << a)) == 0) {
                        int rm = nm | (1 << a);
                        if (findSlot(t, cap, rm, 0)) unite(t, cap, m, rm);
                    }
                }
            } else {
                int nm = m | (1 << b);
                if (findSlot(t, cap, nm, 0)) unite(t, cap, m, nm);
            }
        }
    }
    int groups = 0, maxSize = 0;
    bool* seen = (bool*)calloc((size_t)cap, sizeof(bool));
    for (int ki = 0; ki < kn; ki++) {
        int r = findP(t, cap, keys[ki]);
        Node* rn = findSlot(t, cap, r, 0);
        unsigned idx = hush(r) % (unsigned)cap;
        // mark by root key via linear probe on seen keyed by root
        // use separate hash for seen roots
        unsigned h = hush(r) % (unsigned)cap;
        int found = 0;
        for (int i = 0; i < cap; i++) {
            unsigned ii = (h + i) % (unsigned)cap;
            // reuse: store seen roots in keys array secondary? simpler: scan
        }
        (void)found; (void)idx;
    }
    // recount properly
    int* roots = (int*)malloc((size_t)kn * sizeof(int));
    int rn = 0;
    for (int ki = 0; ki < kn; ki++) {
        int r = findP(t, cap, keys[ki]);
        int exists = 0;
        for (int i = 0; i < rn; i++) if (roots[i] == r) { exists = 1; break; }
        if (!exists) {
            roots[rn++] = r;
            Node* n = findSlot(t, cap, r, 0);
            groups++;
            if (n->size > maxSize) maxSize = n->size;
        }
    }
    free(keys); free(t); free(seen); free(roots);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = groups; ans[1] = maxSize;
    *returnSize = 2;
    return ans;
}
