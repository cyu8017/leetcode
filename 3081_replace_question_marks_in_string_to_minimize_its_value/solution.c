// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

#include <stdlib.h>
#include <string.h>

typedef struct { int v, c; } Pair;
typedef struct { Pair* a; int n; } MinHeap;
static int lessP(Pair x, Pair y) { return x.v < y.v || (x.v == y.v && x.c < y.c); }
static void hpush(MinHeap* h, Pair p) {
    int i = h->n++;
    h->a[i] = p;
    while (i > 0) {
        int par = (i - 1) / 2;
        if (!lessP(h->a[i], h->a[par])) break;
        Pair t = h->a[i]; h->a[i] = h->a[par]; h->a[par] = t; i = par;
    }
}
static Pair hpop(MinHeap* h) {
    Pair r = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l = 2*i+1, rg = 2*i+2, m = i;
        if (l < h->n && lessP(h->a[l], h->a[m])) m = l;
        if (rg < h->n && lessP(h->a[rg], h->a[m])) m = rg;
        if (m == i) break;
        Pair t = h->a[i]; h->a[i] = h->a[m]; h->a[m] = t; i = m;
    }
    return r;
}
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }

char* minimizeStringValue(char* s) {
    int cnt[26] = {0}, k = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] == '?') k++;
        else cnt[s[i] - 'a']++;
    }
    Pair buf[26];
    MinHeap pq = {buf, 0};
    for (int i = 0; i < 26; i++) hpush(&pq, (Pair){cnt[i], i});
    int* t = (int*)malloc((size_t)(k + 1) * sizeof(int));
    for (int i = 0; i < k; i++) {
        Pair p = hpop(&pq);
        t[i] = p.c;
        p.v++;
        hpush(&pq, p);
    }
    qsort(t, (size_t)k, sizeof(int), cmp_int);
    char* cs = (char*)malloc((size_t)n + 1);
    memcpy(cs, s, (size_t)n + 1);
    int j = 0;
    for (int i = 0; i < n; i++) if (cs[i] == '?') cs[i] = (char)(t[j++] + 'a');
    free(t);
    return cs;
}
