// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

typedef struct { int key; int cnt; } Freq;

static int findFreq(Freq* f, int n, int key) {
    for (int i = 0; i < n; i++) if (f[i].key == key) return i;
    return -1;
}

int* recoverArray(int n, int* sums, int sumsSize, int* returnSize) {
    int* cur = (int*)malloc((size_t)sumsSize * sizeof(int));
    memcpy(cur, sums, (size_t)sumsSize * sizeof(int));
    qsort(cur, (size_t)sumsSize, sizeof(int), cmpInt);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int m = sumsSize;
    for (int step = 0; step < n; step++) {
        int d = cur[1] - cur[0];
        Freq* freq = (Freq*)malloc((size_t)m * sizeof(Freq));
        int fn = 0;
        for (int i = 0; i < m; i++) {
            int idx = findFreq(freq, fn, cur[i]);
            if (idx < 0) { freq[fn].key = cur[i]; freq[fn].cnt = 1; fn++; }
            else freq[idx].cnt++;
        }
        int* without = (int*)malloc((size_t)(m / 2) * sizeof(int));
        int* withd = (int*)malloc((size_t)(m / 2) * sizeof(int));
        int wn = 0, wd = 0;
        for (int i = 0; i < m; i++) {
            int idx = findFreq(freq, fn, cur[i]);
            if (idx < 0 || freq[idx].cnt == 0) continue;
            int idx2 = findFreq(freq, fn, cur[i] + d);
            if (idx2 < 0 || freq[idx2].cnt == 0) continue;
            freq[idx].cnt--;
            freq[idx2].cnt--;
            without[wn++] = cur[i];
            withd[wd++] = cur[i] + d;
        }
        int hasZero = 0;
        for (int i = 0; i < wn; i++) if (without[i] == 0) { hasZero = 1; break; }
        free(cur);
        if (hasZero) {
            ans[step] = d;
            cur = without;
            free(withd);
            m = wn;
        } else {
            ans[step] = -d;
            cur = withd;
            free(without);
            m = wd;
        }
        free(freq);
    }
    free(cur);
    *returnSize = n;
    return ans;
}
