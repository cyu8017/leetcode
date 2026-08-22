// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/

#include <stdlib.h>

typedef struct { int k, v; } Pair3960;

static int find3960(Pair3960* a, int an, int k) {
    for (int i = 0; i < an; i++) if (a[i].k == k) return i;
    return -1;
}

int getLength(int* nums, int numsSize) {
    int n = numsSize, ans = 1;
    for (int l = 0; l < n; l++) {
        Pair3960* cnt = malloc((size_t)(n + 1) * sizeof(Pair3960));
        Pair3960* freq = malloc((size_t)(n + 1) * sizeof(Pair3960));
        int cn = 0, fn = 0;
        for (int r = l; r < n; r++) {
            int x = nums[r];
            int ci = find3960(cnt, cn, x);
            int c = ci < 0 ? 0 : cnt[ci].v;
            if (c > 0) {
                int fi = find3960(freq, fn, c);
                if (fi >= 0) {
                    freq[fi].v--;
                    if (freq[fi].v == 0) freq[fi] = freq[--fn];
                }
            }
            if (ci < 0) { cnt[cn].k = x; cnt[cn].v = 1; cn++; }
            else cnt[ci].v = c + 1;
            int cx = c + 1;
            int fi = find3960(freq, fn, cx);
            if (fi < 0) { freq[fn].k = cx; freq[fn].v = 1; fn++; }
            else freq[fi].v++;
            int ok = 0;
            if (cn == 1) ok = 1;
            else if (fn == 2) {
                int f2i = find3960(freq, fn, cx * 2);
                int fhi = (cx % 2 == 0) ? find3960(freq, fn, cx / 2) : -1;
                if ((f2i >= 0 && freq[f2i].v > 0) || (fhi >= 0 && freq[fhi].v > 0)) ok = 1;
            }
            if (ok && r - l + 1 > ans) ans = r - l + 1;
        }
        free(cnt); free(freq);
    }
    return ans;
}
