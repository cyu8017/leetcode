// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int pos, speed, steps; } Node;

int racecar(int target) {
    int qcap = 200000;
    Node* q = (Node*)malloc((size_t)qcap * sizeof(Node));
    int qh = 0, qt = 0;
    int cap = 1 << 20;
    long long* keys = (long long*)malloc((size_t)cap * sizeof(long long));
    bool* used = (bool*)calloc((size_t)cap, sizeof(bool));

    #define KEY(p,s) (((long long)(p) << 20) ^ ((long long)(s) & 0xfffff))
    #define MARK(p,s,ok) do { \
        unsigned h = (unsigned)KEY(p,s) & (cap - 1); \
        long long k = KEY(p,s); ok = true; \
        while (used[h]) { if (keys[h] == k) { ok = false; break; } h = (h + 1) & (cap - 1); } \
        if (ok) { used[h] = true; keys[h] = k; } \
    } while (0)

    bool ok;
    q[qt++] = (Node){0, 1, 0};
    MARK(0, 1, ok);
    while (qh < qt) {
        Node cur = q[qh++];
        if (cur.pos == target) {
            free(q); free(keys); free(used);
            return cur.steps;
        }
        int np = cur.pos + cur.speed, ns = cur.speed * 2;
        if (abs(np) < target * 2) {
            MARK(np, ns, ok);
            if (ok) {
                if (qt == qcap) { qcap *= 2; q = (Node*)realloc(q, (size_t)qcap * sizeof(Node)); }
                q[qt++] = (Node){np, ns, cur.steps + 1};
            }
        }
        int rs = cur.speed > 0 ? -1 : 1;
        MARK(cur.pos, rs, ok);
        if (ok) {
            if (qt == qcap) { qcap *= 2; q = (Node*)realloc(q, (size_t)qcap * sizeof(Node)); }
            q[qt++] = (Node){cur.pos, rs, cur.steps + 1};
        }
    }
    free(q); free(keys); free(used);
    return -1;
#undef KEY
#undef MARK
}
