// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int cost, val; } Item;
static void heap_up(Item* h, int i) {
    while (i > 0) { int p = (i - 1) / 2; if (h[p].cost <= h[i].cost) break; Item t = h[p]; h[p] = h[i]; h[i] = t; i = p; }
}
static void heap_down(Item* h, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < n && h[l].cost < h[s].cost) s = l;
        if (r < n && h[r].cost < h[s].cost) s = r;
        if (s == i) break;
        Item t = h[s]; h[s] = h[i]; h[i] = t; i = s;
    }
}
static bool* sieve(int n) {
    bool* p = (bool*)malloc(n); memset(p, 1, n); p[0] = p[1] = false;
    for (int i = 2; i * i < n; i++) if (p[i]) for (int j = i * i; j < n; j += i) p[j] = false;
    return p;
}
static void itoa_buf(int x, char* s, int* len) {
    if (x == 0) { s[0] = '0'; *len = 1; return; }
    char tmp[16]; int n = 0;
    while (x > 0) { tmp[n++] = '0' + x % 10; x /= 10; }
    for (int i = 0; i < n; i++) s[i] = tmp[n - 1 - i];
    *len = n;
}
static int atoi_buf(char* s, int len) { int v = 0; for (int i = 0; i < len; i++) v = v * 10 + s[i] - '0'; return v; }

int minOperations(int n, int m) {
    bool* isPrime = sieve(100000);
    if (isPrime[n]) { free(isPrime); return -1; }
    int* dist = (int*)malloc(100000 * sizeof(int));
    for (int i = 0; i < 100000; i++) dist[i] = -1;
    int cap = 256, hn = 0;
    Item* heap = (Item*)malloc(cap * sizeof(Item));
    heap[hn++] = (Item){n, n}; dist[n] = n;
    int ans = -1;
    while (hn > 0) {
        Item cur = heap[0]; heap[0] = heap[--hn]; if (hn) heap_down(heap, hn, 0);
        if (cur.cost != dist[cur.val]) continue;
        if (cur.val == m) { ans = cur.cost; break; }
        char s[16]; int len; itoa_buf(cur.val, s, &len);
        for (int i = 0; i < len; i++) {
            char orig = s[i];
            for (int d = -1; d <= 1; d += 2) {
                int nd = (orig - '0') + d;
                if (nd < 0 || nd > 9) continue;
                if (i == 0 && nd == 0 && len > 1) continue;
                s[i] = '0' + nd;
                int nv = atoi_buf(s, len);
                s[i] = orig;
                if (isPrime[nv]) continue;
                int nc = cur.cost + nv;
                if (dist[nv] == -1 || nc < dist[nv]) {
                    dist[nv] = nc;
                    if (hn == cap) { cap *= 2; heap = (Item*)realloc(heap, cap * sizeof(Item)); }
                    heap[hn] = (Item){nc, nv}; heap_up(heap, hn); hn++;
                }
            }
        }
    }
    free(isPrime); free(dist); free(heap);
    return ans;
}
