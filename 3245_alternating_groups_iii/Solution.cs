// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

using System;
using System.Collections.Generic;

public class Solution {
    class SegTree {
        int n;
        int[] treeIntervalCounts, treeIntervalLengths;
        public SegTree(int n_) {
            n = n_;
            treeIntervalCounts = new int[4 * n_];
            treeIntervalLengths = new int[4 * n_];
        }
        public void Add(int i, int val) => AddRec(0, 0, n - 1, i, val);
        void AddRec(int treeIndex, int lo, int hi, int i, int val) {
            if (lo == hi) {
                treeIntervalCounts[treeIndex] += val;
                treeIntervalLengths[treeIndex] = treeIntervalCounts[treeIndex] * i;
                return;
            }
            int mid = (lo + hi) / 2;
            if (i <= mid) AddRec(2 * treeIndex + 1, lo, mid, i, val);
            else AddRec(2 * treeIndex + 2, mid + 1, hi, i, val);
            treeIntervalCounts[treeIndex] = treeIntervalCounts[2 * treeIndex + 1] + treeIntervalCounts[2 * treeIndex + 2];
            treeIntervalLengths[treeIndex] = treeIntervalLengths[2 * treeIndex + 1] + treeIntervalLengths[2 * treeIndex + 2];
        }
        public int QueryIntervalCounts(int i) => Query(treeIntervalCounts, 0, 0, n - 1, i, n - 1);
        public int QueryIntervalLengths(int i) => Query(treeIntervalLengths, 0, 0, n - 1, i, n - 1);
        int Query(int[] tree, int treeIndex, int lo, int hi, int i, int j) {
            if (i <= lo && hi <= j) return tree[treeIndex];
            if (j < lo || hi < i) return 0;
            int mid = (lo + hi) / 2;
            return Query(tree, treeIndex * 2 + 1, lo, mid, i, j) + Query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j);
        }
    }

    public int[] NumberOfAlternatingGroups(int[] colors, int[][] queries) {
        int n = colors.Length;
        var ans = new List<int>();
        var arr = new List<int>(colors);
        for (int i = 0; i < n - 1; i++) arr.Add(colors[i]);
        var tree = new SegTree(2 * n - 1);
        var intervals = new SortedSet<(int, int)>();

        void Insert(int l, int r) {
            intervals.Add((l, r));
            if (l < n) tree.Add(r - l + 1, 1);
        }
        void Remove(int l, int r) {
            intervals.Remove((l, r));
            if (l < n) tree.Add(r - l + 1, -1);
        }
        (int, int) FindInterval(int target) {
            int bestL = -1, bestR = -1;
            foreach (var k in intervals) {
                if (k.Item1 <= target && target <= k.Item2) {
                    if (k.Item1 > bestL) {
                        bestL = k.Item1;
                        bestR = k.Item2;
                    }
                }
            }
            return (bestL, bestR);
        }
        int GetNum(int sz) {
            int numIntervals = tree.QueryIntervalCounts(sz);
            int sumIntervals = tree.QueryIntervalLengths(sz);
            int numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals;
            var (l, r) = FindInterval(n);
            if (l < 0 || l >= n || r - l + 1 < sz) return numAlternatingGroups;
            if (r >= n) {
                int nonDuplicateGroups = n - l;
                int numGroups = (r - l + 1) - sz + 1;
                int extra = numGroups - nonDuplicateGroups;
                if (extra > 0) numAlternatingGroups -= extra;
            }
            return numAlternatingGroups;
        }
        void Update(int index, int color) {
            if (arr[index] == color) return;
            arr[index] = color;
            var (start, end) = FindInterval(index);
            Remove(start, end);
            if (start < index && index < end) {
                Insert(start, index - 1);
                Insert(index, index);
                Insert(index + 1, end);
                return;
            }
            if (start == index && index < end) Insert(start + 1, end);
            if (start < index && index == end) Insert(start, end - 1);
            int ns = index, ne = index;
            for (;;) {
                bool merged = false;
                foreach (var k in intervals) {
                    if (k.Item2 + 1 == ns && arr[k.Item2] != arr[ns]) {
                        Remove(k.Item1, k.Item2);
                        ns = k.Item1;
                        merged = true;
                        break;
                    }
                }
                if (!merged) break;
            }
            for (;;) {
                bool merged = false;
                foreach (var k in intervals) {
                    if (k.Item1 == ne + 1 && arr[k.Item1] != arr[ne]) {
                        Remove(k.Item1, k.Item2);
                        ne = k.Item2;
                        merged = true;
                        break;
                    }
                }
                if (!merged) break;
            }
            Insert(ns, ne);
        }

        int st = 0;
        for (int i = 1; i < 2 * n - 1; i++) {
            if (arr[i] == arr[i - 1]) {
                Insert(st, i - 1);
                st = i;
            }
        }
        Insert(st, 2 * n - 2);

        foreach (var query in queries) {
            if (query[0] == 1) ans.Add(GetNum(query[1]));
            else {
                int index = query[1], color = query[2];
                if (arr[index] != color) {
                    Update(index, color);
                    if (index < n - 1) Update(index + n, color);
                }
            }
        }
        return ans.ToArray();
    }
}
