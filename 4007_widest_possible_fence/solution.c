// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

#include <stdlib.h>

typedef struct {
    int key, val;
} KV4007;

static int findKV4007(KV4007* a, int n, int key) {
    for (int i = 0; i < n; i++) if (a[i].key == key) return i;
    return -1;
}

static void addKV4007(KV4007** a, int* n, int* cap, int key, int delta, int* ans) {
    int idx = findKV4007(*a, *n, key);
    if (idx < 0) {
        if (*n == *cap) {
            *cap = *cap ? *cap * 2 : 16;
            *a = (KV4007*)realloc(*a, (size_t)(*cap) * sizeof(KV4007));
        }
        idx = (*n)++;
        (*a)[idx].key = key;
        (*a)[idx].val = 0;
    }
    (*a)[idx].val += delta;
    if ((*a)[idx].val > *ans) *ans = (*a)[idx].val;
}

int maximumWidth(int* planks, int planksSize) {
    KV4007* cnt = NULL;
    int cn = 0, ccap = 0;
    for (int i = 0; i < planksSize; i++) {
        int idx = findKV4007(cnt, cn, planks[i]);
        if (idx < 0) {
            if (cn == ccap) {
                ccap = ccap ? ccap * 2 : 16;
                cnt = (KV4007*)realloc(cnt, (size_t)ccap * sizeof(KV4007));
            }
            cnt[cn].key = planks[i];
            cnt[cn].val = 1;
            cn++;
        } else {
            cnt[idx].val++;
        }
    }

    KV4007* t = NULL;
    int tn = 0, tcap = 0;
    int ans = 0;

    for (int i = 0; i < cn; i++) {
        int x = cnt[i].key, v1 = cnt[i].val;
        addKV4007(&t, &tn, &tcap, x, v1, &ans);
        addKV4007(&t, &tn, &tcap, x * 2, v1 / 2, &ans);
        for (int j = 0; j < cn; j++) {
            int y = cnt[j].key, v2 = cnt[j].val;
            if (y > x) {
                int add = v1 < v2 ? v1 : v2;
                addKV4007(&t, &tn, &tcap, x + y, add, &ans);
            }
        }
    }

    free(cnt);
    free(t);
    return ans;
}
