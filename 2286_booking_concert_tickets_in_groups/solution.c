// LeetCode 2286 - Booking Concert Tickets in Groups
// https://leetcode.com/problems/booking-concert-tickets-in-groups/

#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    long long sum;
    long long mx;
} SegNode;

typedef struct {
    int n, m;
    SegNode* tree;
} BookMyShow;

static void pull(BookMyShow* obj, int idx) {
    obj->tree[idx].sum = obj->tree[idx * 2].sum + obj->tree[idx * 2 + 1].sum;
    long long a = obj->tree[idx * 2].mx, b = obj->tree[idx * 2 + 1].mx;
    obj->tree[idx].mx = a > b ? a : b;
}

static void build(BookMyShow* obj, int idx, int l, int r) {
    if (l == r) {
        obj->tree[idx].sum = obj->m;
        obj->tree[idx].mx = obj->m;
        return;
    }
    int mid = (l + r) / 2;
    build(obj, idx * 2, l, mid);
    build(obj, idx * 2 + 1, mid + 1, r);
    pull(obj, idx);
}

static void update(BookMyShow* obj, int idx, int l, int r, int pos, long long val) {
    if (l == r) {
        obj->tree[idx].sum = val;
        obj->tree[idx].mx = val;
        return;
    }
    int mid = (l + r) / 2;
    if (pos <= mid) update(obj, idx * 2, l, mid, pos, val);
    else update(obj, idx * 2 + 1, mid + 1, r, pos, val);
    pull(obj, idx);
}

static long long querySum(BookMyShow* obj, int idx, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return obj->tree[idx].sum;
    int mid = (l + r) / 2;
    return querySum(obj, idx * 2, l, mid, ql, qr) + querySum(obj, idx * 2 + 1, mid + 1, r, ql, qr);
}

static int findFirst(BookMyShow* obj, int idx, int l, int r, int maxRow, long long k) {
    if (l > maxRow || obj->tree[idx].mx < k) return -1;
    if (l == r) return l;
    int mid = (l + r) / 2;
    int left = findFirst(obj, idx * 2, l, mid, maxRow, k);
    if (left != -1) return left;
    return findFirst(obj, idx * 2 + 1, mid + 1, r, maxRow, k);
}

BookMyShow* bookMyShowCreate(int n, int m) {
    BookMyShow* obj = (BookMyShow*)malloc(sizeof(BookMyShow));
    obj->n = n;
    obj->m = m;
    obj->tree = (SegNode*)calloc((size_t)(4 * n), sizeof(SegNode));
    build(obj, 1, 0, n - 1);
    return obj;
}

int* bookMyShowGather(BookMyShow* obj, int k, int maxRow, int* returnSize) {
    int row = findFirst(obj, 1, 0, obj->n - 1, maxRow, k);
    if (row == -1) {
        *returnSize = 0;
        return NULL;
    }
    long long remain = querySum(obj, 1, 0, obj->n - 1, row, row);
    int seat = (int)((long long)obj->m - remain);
    update(obj, 1, 0, obj->n - 1, row, remain - k);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = row;
    ans[1] = seat;
    *returnSize = 2;
    return ans;
}

bool bookMyShowScatter(BookMyShow* obj, int k, int maxRow) {
    if (querySum(obj, 1, 0, obj->n - 1, 0, maxRow) < k) return false;
    long long need = k;
    for (int row = 0; row <= maxRow && need > 0; row++) {
        long long remain = querySum(obj, 1, 0, obj->n - 1, row, row);
        if (remain == 0) continue;
        long long take = remain;
        if (take > need) take = need;
        update(obj, 1, 0, obj->n - 1, row, remain - take);
        need -= take;
    }
    return true;
}

void bookMyShowFree(BookMyShow* obj) {
    free(obj->tree);
    free(obj);
}
