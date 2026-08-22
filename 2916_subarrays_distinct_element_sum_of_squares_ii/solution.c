// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { int sum, sumSq, lazy; } Node;

static Node* tree;
static const int MOD = 1000000007;

static void apply(int idx, int l, int r, int val) {
    int length = r - l + 1;
    tree[idx].sumSq = (int)((tree[idx].sumSq + 2LL * val % MOD * tree[idx].sum % MOD + 1LL * val % MOD * val % MOD * length % MOD) % MOD);
    tree[idx].sum = (int)((tree[idx].sum + 1LL * val % MOD * length % MOD) % MOD);
    tree[idx].lazy = (tree[idx].lazy + val) % MOD;
}

static void push(int idx, int l, int r) {
    if (tree[idx].lazy != 0 && l != r) {
        int mid = (l + r) / 2;
        apply(idx * 2, l, mid, tree[idx].lazy);
        apply(idx * 2 + 1, mid + 1, r, tree[idx].lazy);
        tree[idx].lazy = 0;
    }
}

static void update(int idx, int l, int r, int ql, int qr, int val) {
    if (ql > r || qr < l) return;
    if (ql <= l && r <= qr) { apply(idx, l, r, val); return; }
    push(idx, l, r);
    int mid = (l + r) / 2;
    update(idx * 2, l, mid, ql, qr, val);
    update(idx * 2 + 1, mid + 1, r, ql, qr, val);
    tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD;
    tree[idx].sumSq = (tree[idx * 2].sumSq + tree[idx * 2 + 1].sumSq) % MOD;
}

int sumCounts(int* nums, int numsSize) {
    int n = numsSize;
    tree = (Node*)calloc(4 * (n + 2), sizeof(Node));
    int* last = (int*)calloc(100001, sizeof(int)); /* values up to 1e5 typically; fallback map via array of pairs */
    /* Use dynamic last map via linear search on pairs for safety */
    typedef struct { int key, val; } KV;
    KV* lastm = (KV*)malloc(n * sizeof(KV));
    int ln = 0;
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        int v = nums[i - 1], prev = 0;
        for (int j = 0; j < ln; j++) if (lastm[j].key == v) { prev = lastm[j].val; break; }
        update(1, 1, n, prev + 1, i, 1);
        ans = (ans + tree[1].sumSq) % MOD;
        int found = 0;
        for (int j = 0; j < ln; j++) if (lastm[j].key == v) { lastm[j].val = i; found = 1; break; }
        if (!found) { lastm[ln].key = v; lastm[ln].val = i; ln++; }
    }
    free(tree); free(last); free(lastm);
    return ans;
}
