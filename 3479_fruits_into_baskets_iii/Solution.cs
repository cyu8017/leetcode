// LeetCode 3479 - Fruits Into Baskets III
// https://leetcode.com/problems/fruits-into-baskets-iii/

using System;

public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        int n = baskets.Length;
        int size = 1;
        while (size < n) size <<= 1;
        int[] tree = new int[size * 2];
        for (int i = 0; i < n; i++) tree[size + i] = baskets[i];
        for (int i = size - 1; i > 0; i--) tree[i] = Math.Max(tree[i * 2], tree[i * 2 + 1]);
        int Find(int node, int nl, int nr, int need) {
            if (tree[node] < need) return -1;
            if (nl == nr) return nl;
            int mid = (nl + nr) / 2;
            int left = Find(node * 2, nl, mid, need);
            if (left != -1) return left;
            return Find(node * 2 + 1, mid + 1, nr, need);
        }
        void Update(int idx) {
            int p = size + idx;
            tree[p] = -1;
            for (p >>= 1; p > 0; p >>= 1) tree[p] = Math.Max(tree[p * 2], tree[p * 2 + 1]);
        }
        int unplaced = 0;
        foreach (int f in fruits) {
            int idx = Find(1, 0, size - 1, f);
            if (idx == -1 || idx >= n) unplaced++;
            else Update(idx);
        }
        return unplaced;
    }
}
