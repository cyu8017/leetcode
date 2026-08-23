// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

class Solution {
    private static class SegTree {
        int n;
        int[] treeIntervalCounts, treeIntervalLengths;

        SegTree(int n_) {
            n = n_;
            treeIntervalCounts = new int[4 * n_];
            treeIntervalLengths = new int[4 * n_];
        }

        void add(int i, int val) {
            addRec(0, 0, n - 1, i, val);
        }

        void addRec(int treeIndex, int lo, int hi, int i, int val) {
            if (lo == hi) {
                treeIntervalCounts[treeIndex] += val;
                treeIntervalLengths[treeIndex] = treeIntervalCounts[treeIndex] * i;
                return;
            }
            int mid = (lo + hi) / 2;
            if (i <= mid) {
                addRec(2 * treeIndex + 1, lo, mid, i, val);
            } else {
                addRec(2 * treeIndex + 2, mid + 1, hi, i, val);
            }
            treeIntervalCounts[treeIndex] = treeIntervalCounts[2 * treeIndex + 1] + treeIntervalCounts[2 * treeIndex + 2];
            treeIntervalLengths[treeIndex] = treeIntervalLengths[2 * treeIndex + 1] + treeIntervalLengths[2 * treeIndex + 2];
        }

        int queryIntervalCounts(int i) {
            return query(treeIntervalCounts, 0, 0, n - 1, i, n - 1);
        }

        int queryIntervalLengths(int i) {
            return query(treeIntervalLengths, 0, 0, n - 1, i, n - 1);
        }

        int query(int[] tree, int treeIndex, int lo, int hi, int i, int j) {
            if (i <= lo && hi <= j) {
                return tree[treeIndex];
            }
            if (j < lo || hi < i) {
                return 0;
            }
            int mid = (lo + hi) / 2;
            return query(tree, treeIndex * 2 + 1, lo, mid, i, j)
                    + query(tree, treeIndex * 2 + 2, mid + 1, hi, i, j);
        }
    }

    private static long pack(int l, int r) {
        return (((long) l) << 32) | (r & 0xffffffffL);
    }

    private static int unpackL(long v) {
        return (int) (v >> 32);
    }

    private static int unpackR(long v) {
        return (int) v;
    }

    public int[] numberOfAlternatingGroups(int[] colors, int[][] queries) {
        int n = colors.length;
        List<Integer> ans = new ArrayList<>();
        int[] arr = new int[2 * n - 1];
        for (int i = 0; i < n; i++) {
            arr[i] = colors[i];
        }
        for (int i = 0; i < n - 1; i++) {
            arr[n + i] = colors[i];
        }
        SegTree tree = new SegTree(2 * n - 1);
        TreeSet<Long> intervals = new TreeSet<>();

        class Ops {
            void insert(int l, int r) {
                intervals.add(pack(l, r));
                if (l < n) {
                    tree.add(r - l + 1, 1);
                }
            }

            void remove(int l, int r) {
                intervals.remove(pack(l, r));
                if (l < n) {
                    tree.add(r - l + 1, -1);
                }
            }

            int[] findInterval(int target) {
                int bestL = -1, bestR = -1;
                for (long k : intervals) {
                    int kl = unpackL(k), kr = unpackR(k);
                    if (kl <= target && target <= kr) {
                        if (kl > bestL) {
                            bestL = kl;
                            bestR = kr;
                        }
                    }
                }
                return new int[] {bestL, bestR};
            }

            int getNum(int sz) {
                int numIntervals = tree.queryIntervalCounts(sz);
                int sumIntervals = tree.queryIntervalLengths(sz);
                int numAlternatingGroups = sumIntervals - numIntervals * sz + numIntervals;
                int[] lr = findInterval(n);
                int l = lr[0], r = lr[1];
                if (l < 0 || l >= n || r - l + 1 < sz) {
                    return numAlternatingGroups;
                }
                if (r >= n) {
                    int nonDuplicateGroups = n - l;
                    int numGroups = (r - l + 1) - sz + 1;
                    int extra = numGroups - nonDuplicateGroups;
                    if (extra > 0) {
                        numAlternatingGroups -= extra;
                    }
                }
                return numAlternatingGroups;
            }

            void update(int index, int color) {
                if (arr[index] == color) {
                    return;
                }
                arr[index] = color;
                int[] se = findInterval(index);
                int start = se[0], end = se[1];
                remove(start, end);
                if (start < index && index < end) {
                    insert(start, index - 1);
                    insert(index, index);
                    insert(index + 1, end);
                    return;
                }
                if (start == index && index < end) {
                    insert(start + 1, end);
                }
                if (start < index && index == end) {
                    insert(start, end - 1);
                }
                int ns = index, ne = index;
                for (;;) {
                    boolean merged = false;
                    for (long k : new ArrayList<>(intervals)) {
                        int kl = unpackL(k), kr = unpackR(k);
                        if (kr + 1 == ns && arr[kr] != arr[ns]) {
                            remove(kl, kr);
                            ns = kl;
                            merged = true;
                            break;
                        }
                    }
                    if (!merged) {
                        break;
                    }
                }
                for (;;) {
                    boolean merged = false;
                    for (long k : new ArrayList<>(intervals)) {
                        int kl = unpackL(k), kr = unpackR(k);
                        if (kl == ne + 1 && arr[kl] != arr[ne]) {
                            remove(kl, kr);
                            ne = kr;
                            merged = true;
                            break;
                        }
                    }
                    if (!merged) {
                        break;
                    }
                }
                insert(ns, ne);
            }
        }

        Ops ops = new Ops();
        int st = 0;
        for (int i = 1; i < 2 * n - 1; i++) {
            if (arr[i] == arr[i - 1]) {
                ops.insert(st, i - 1);
                st = i;
            }
        }
        ops.insert(st, 2 * n - 2);

        for (int[] query : queries) {
            if (query[0] == 1) {
                ans.add(ops.getNum(query[1]));
            } else {
                int index = query[1], color = query[2];
                if (arr[index] != color) {
                    ops.update(index, color);
                    if (index < n - 1) {
                        ops.update(index + n, color);
                    }
                }
            }
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            res[i] = ans.get(i);
        }
        return res;
    }
}
