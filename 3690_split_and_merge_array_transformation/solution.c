// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int a[6]; } Arr6;

#define VIS_CAP 10007
typedef struct { Arr6 key; int used; } VisSlot;
static VisSlot vis[VIS_CAP];

static unsigned hashArr(Arr6 t, int n) {
    unsigned h = 0;
    for (int i = 0; i < n; i++) h = h * 31u + (unsigned)(t.a[i] + 1000);
    return h % VIS_CAP;
}

static bool visHas(Arr6 t, int n) {
    unsigned i = hashArr(t, n);
    for (int k = 0; k < VIS_CAP; k++) {
        unsigned j = (i + k) % VIS_CAP;
        if (!vis[j].used) return false;
        if (memcmp(vis[j].key.a, t.a, (size_t)n * sizeof(int)) == 0) return true;
    }
    return true;
}

static void visAdd(Arr6 t, int n) {
    unsigned i = hashArr(t, n);
    for (int k = 0; k < VIS_CAP; k++) {
        unsigned j = (i + k) % VIS_CAP;
        if (!vis[j].used) { vis[j].used = 1; vis[j].key = t; return; }
        if (memcmp(vis[j].key.a, t.a, (size_t)n * sizeof(int)) == 0) return;
    }
}

static bool arrEq(Arr6 a, Arr6 b, int n) {
    return memcmp(a.a, b.a, (size_t)n * sizeof(int)) == 0;
}

int minSplitMerge(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    memset(vis, 0, sizeof(vis));
    Arr6 start = {{0}}, target = {{0}};
    for (int i = 0; i < n; i++) { start.a[i] = nums1[i]; target.a[i] = nums2[i]; }
    Arr6* q = (Arr6*)malloc(200000 * sizeof(Arr6));
    int qn = 0;
    q[qn++] = start;
    visAdd(start, n);
    for (int ans = 0; ; ans++) {
        Arr6* nq = (Arr6*)malloc(200000 * sizeof(Arr6));
        int nn = 0;
        for (int qi = 0; qi < qn; qi++) {
            Arr6 cur = q[qi];
            if (arrEq(cur, target, n)) { free(q); free(nq); return ans; }
            for (int l = 0; l < n; l++) {
                for (int r = l; r < n; r++) {
                    int remain[6], rn = 0;
                    int sub[6], sn = 0;
                    for (int i = 0; i < l; i++) remain[rn++] = cur.a[i];
                    for (int i = r + 1; i < n; i++) remain[rn++] = cur.a[i];
                    for (int i = l; i <= r; i++) sub[sn++] = cur.a[i];
                    for (int pos = 0; pos <= rn; pos++) {
                        Arr6 nxt = {{0}};
                        int p = 0;
                        for (int i = 0; i < pos; i++) nxt.a[p++] = remain[i];
                        for (int i = 0; i < sn; i++) nxt.a[p++] = sub[i];
                        for (int i = pos; i < rn; i++) nxt.a[p++] = remain[i];
                        if (!visHas(nxt, n)) {
                            visAdd(nxt, n);
                            nq[nn++] = nxt;
                        }
                    }
                }
            }
        }
        free(q);
        q = nq;
        qn = nn;
    }
}
