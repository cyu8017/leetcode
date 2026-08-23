// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

class Solution {
    private int[] tree;
    private int size, n;

    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        n = baskets.length;
        size = 1;
        while (size < n) size <<= 1;
        tree = new int[size * 2];
        for (int i = 0; i < n; i++) tree[size + i] = baskets[i];
        for (int i = size - 1; i > 0; i--) tree[i] = Math.max(tree[i * 2], tree[i * 2 + 1]);
        int unplaced = 0;
        for (int f : fruits) {
            int idx = find(1, 0, size - 1, f);
            if (idx == -1 || idx >= n) unplaced++;
            else update(idx);
        }
        return unplaced;
    }

    private int find(int node, int nl, int nr, int need) {
        if (tree[node] < need) return -1;
        if (nl == nr) return nl;
        int mid = (nl + nr) / 2;
        int left = find(node * 2, nl, mid, need);
        if (left != -1) return left;
        return find(node * 2 + 1, mid + 1, nr, need);
    }

    private void update(int idx) {
        int p = size + idx;
        tree[p] = -1;
        for (p >>= 1; p > 0; p >>= 1) tree[p] = Math.max(tree[p * 2], tree[p * 2 + 1]);
    }
}
