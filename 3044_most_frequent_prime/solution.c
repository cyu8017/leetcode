// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key, val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static void hinc(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val++; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = 1;
}
static bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i <= n / i; i++) if (n % i == 0) return false;
    return true;
}

int mostFrequentPrime(int** mat, int matSize, int* matColSize) {
    int m = matSize, n = matColSize[0];
    int cap = 1 << 16;
    HEnt* t = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            for (int a = -1; a <= 1; a++) for (int b = -1; b <= 1; b++) {
                if (a == 0 && b == 0) continue;
                int x = i + a, y = j + b, v = mat[i][j];
                while (x >= 0 && x < m && y >= 0 && y < n) {
                    v = v * 10 + mat[x][y];
                    if (isPrime(v)) hinc(t, cap, v);
                    x += a; y += b;
                }
            }
        }
    }
    int ans = -1, mx = 0;
    for (int i = 0; i < cap; i++) if (t[i].used) {
        if (t[i].val > mx || (t[i].val == mx && t[i].key > ans)) {
            mx = t[i].val; ans = t[i].key;
        }
    }
    free(t);
    return ans;
}
