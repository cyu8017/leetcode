// LeetCode 2276 - Count Integers in Intervals
// https://leetcode.com/problems/count-integers-in-intervals/

#include <stdlib.h>
#include <stdbool.h>

typedef struct SegNode {
    struct SegNode* left;
    struct SegNode* right;
    bool covered;
} SegNode;

typedef struct {
    SegNode* root;
    int cnt;
} CountIntervals;

static int add_seg(int L, int R, int l, int r, SegNode** node) {
    if (*node == NULL) *node = (SegNode*)calloc(1, sizeof(SegNode));
    SegNode* n = *node;
    if (n->covered) return 0;
    if (l <= L && R <= r) {
        n->covered = true;
        n->left = n->right = NULL;
        return R - L + 1;
    }
    int mid = L + (R - L) / 2;
    int added = 0;
    if (l <= mid) added += add_seg(L, mid, l, r, &n->left);
    if (r > mid) added += add_seg(mid + 1, R, l, r, &n->right);
    if (n->left && n->right && n->left->covered && n->right->covered) {
        n->covered = true;
        n->left = n->right = NULL;
    }
    return added;
}

static void free_seg(SegNode* n) {
    if (!n) return;
    free_seg(n->left);
    free_seg(n->right);
    free(n);
}

CountIntervals* countIntervalsCreate() {
    return (CountIntervals*)calloc(1, sizeof(CountIntervals));
}

void countIntervalsAdd(CountIntervals* obj, int left, int right) {
    obj->cnt += add_seg(1, 1000000000, left, right, &obj->root);
}

int countIntervalsCount(CountIntervals* obj) {
    return obj->cnt;
}

void countIntervalsFree(CountIntervals* obj) {
    free_seg(obj->root);
    free(obj);
}
