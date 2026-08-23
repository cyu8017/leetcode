// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

using System;

public class Solution {
    class Node {
        public int l, r, g;
    }

    class SegmentTree {
        public Node[] tr;
        public SegmentTree(int n) {
            tr = new Node[n << 2];
            for (int i = 0; i < tr.Length; i++) tr[i] = new Node();
            Build(1, 1, n);
        }
        void Build(int u, int l, int r) {
            tr[u].l = l; tr[u].r = r; tr[u].g = 0;
            if (l == r) return;
            int mid = (l + r) >> 1;
            Build(u << 1, l, mid);
            Build(u << 1 | 1, mid + 1, r);
        }
        void Pushup(int u) { tr[u].g = Gcd(tr[u << 1].g, tr[u << 1 | 1].g); }
        public void Modify(int u, int x, int v) {
            if (tr[u].l == tr[u].r) { tr[u].g = v; return; }
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (x <= mid) Modify(u << 1, x, v);
            else Modify(u << 1 | 1, x, v);
            Pushup(u);
        }
        public int Query(int u, int l, int r) {
            if (l > r) return 0;
            if (tr[u].l >= l && tr[u].r <= r) return tr[u].g;
            int mid = (tr[u].l + tr[u].r) >> 1;
            if (r <= mid) return Query(u << 1, l, r);
            if (l > mid) return Query(u << 1 | 1, l, r);
            return Gcd(Query(u << 1, l, mid), Query(u << 1 | 1, mid + 1, r));
        }
        static int Gcd(int a, int b) {
            while (b != 0) { int t = a % b; a = b; b = t; }
            return a;
        }
    }

    public int CountGoodSubseq(int[] nums, int p, int[][] queries) {
        int n = nums.Length;
        var tree = new SegmentTree(n);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] % p == 0) {
                tree.Modify(1, i + 1, nums[i]);
                cnt++;
            }
        }
        int ans = 0;
        foreach (var q in queries) {
            int idx = q[0], val = q[1];
            if (nums[idx] % p == 0) {
                tree.Modify(1, idx + 1, 0);
                cnt--;
            }
            if (val % p == 0) {
                tree.Modify(1, idx + 1, val);
                cnt++;
            }
            nums[idx] = val;
            if (tree.tr[1].g != p) continue;
            if (cnt < n || n > 6) {
                ans++;
                continue;
            }
            for (int i = 1; i <= n; i++) {
                int leftG = tree.Query(1, 1, i - 1);
                int rightG = tree.Query(1, i + 1, n);
                int g = leftG;
                int b = rightG;
                while (b != 0) { int t = g % b; g = b; b = t; }
                if (g == p) { ans++; break; }
            }
        }
        return ans;
    }
}
