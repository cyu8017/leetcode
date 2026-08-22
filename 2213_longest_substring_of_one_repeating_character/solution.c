// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char lChar, rChar;
    int lLen, rLen, best, size;
} Seg;

static Seg mergeSeg(Seg a, Seg b) {
    if (a.size == 0) return b;
    if (b.size == 0) return a;
    Seg res = { .lChar = a.lChar, .rChar = b.rChar, .size = a.size + b.size, .best = a.best };
    if (b.best > res.best) res.best = b.best;
    res.lLen = a.lLen;
    res.rLen = b.rLen;
    if (a.rChar == b.lChar) {
        int mid = a.rLen + b.lLen;
        if (mid > res.best) res.best = mid;
        if (a.lLen == a.size) res.lLen = a.size + b.lLen;
        if (b.rLen == b.size) res.rLen = b.size + a.rLen;
    }
    return res;
}

typedef struct {
    int n;
    Seg* tree;
    char* s;
} SegTree;

static void build(SegTree* st, int idx, int l, int r) {
    if (l == r) {
        st->tree[idx] = (Seg){st->s[l], st->s[l], 1, 1, 1, 1};
        return;
    }
    int mid = (l + r) / 2;
    build(st, idx * 2, l, mid);
    build(st, idx * 2 + 1, mid + 1, r);
    st->tree[idx] = mergeSeg(st->tree[idx * 2], st->tree[idx * 2 + 1]);
}

static void update(SegTree* st, int idx, int l, int r, int pos, char ch) {
    if (l == r) {
        st->s[pos] = ch;
        st->tree[idx] = (Seg){ch, ch, 1, 1, 1, 1};
        return;
    }
    int mid = (l + r) / 2;
    if (pos <= mid) update(st, idx * 2, l, mid, pos, ch);
    else update(st, idx * 2 + 1, mid + 1, r, pos, ch);
    st->tree[idx] = mergeSeg(st->tree[idx * 2], st->tree[idx * 2 + 1]);
}

int* longestRepeating(char* s, char* queryCharacters, int* queryIndices, int queryIndicesSize, int* returnSize) {
    int n = (int)strlen(s);
    SegTree st;
    st.n = n;
    st.tree = (Seg*)calloc((size_t)(4 * n + 5), sizeof(Seg));
    st.s = (char*)malloc((size_t)n + 1);
    memcpy(st.s, s, (size_t)n + 1);
    build(&st, 1, 0, n - 1);
    int* ans = (int*)malloc((size_t)queryIndicesSize * sizeof(int));
    for (int i = 0; i < queryIndicesSize; i++) {
        update(&st, 1, 0, n - 1, queryIndices[i], queryCharacters[i]);
        ans[i] = st.tree[1].best;
    }
    free(st.tree); free(st.s);
    *returnSize = queryIndicesSize;
    return ans;
}
