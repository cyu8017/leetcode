// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

#include <stdlib.h>

static int* tree3479;
static int size3479;

static int find3479(int node, int nl, int nr, int need) {
    if (tree3479[node] < need) return -1;
    if (nl == nr) return nl;
    int mid = (nl + nr) / 2;
    int left = find3479(node * 2, nl, mid, need);
    if (left != -1) return left;
    return find3479(node * 2 + 1, mid + 1, nr, need);
}

static void update3479(int idx) {
    int p = size3479 + idx;
    tree3479[p] = -1;
    for (p >>= 1; p > 0; p >>= 1) {
        tree3479[p] = tree3479[p * 2];
        if (tree3479[p * 2 + 1] > tree3479[p]) tree3479[p] = tree3479[p * 2 + 1];
    }
}

int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    int n = basketsSize;
    size3479 = 1;
    while (size3479 < n) size3479 <<= 1;
    tree3479 = (int*)calloc((size_t)(size3479 * 2), sizeof(int));
    for (int i = 0; i < n; i++) tree3479[size3479 + i] = baskets[i];
    for (int i = size3479 - 1; i > 0; i--) {
        tree3479[i] = tree3479[i * 2];
        if (tree3479[i * 2 + 1] > tree3479[i]) tree3479[i] = tree3479[i * 2 + 1];
    }
    int unplaced = 0;
    for (int i = 0; i < fruitsSize; i++) {
        int idx = find3479(1, 0, size3479 - 1, fruits[i]);
        if (idx == -1 || idx >= n) unplaced++;
        else update3479(idx);
    }
    free(tree3479);
    return unplaced;
}
