// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

use std::collections::HashMap;

struct Node {
    l: i32,
    r: i32,
    mn: i32,
    mx: i32,
    lazy: i32,
}

struct SegmentTree {
    tr: Vec<Node>,
}

impl SegmentTree {
    fn new(n: i32) -> Self {
        let mut st = Self {
            tr: (0..(n << 2) as usize)
                .map(|_| Node {
                    l: 0,
                    r: 0,
                    mn: 0,
                    mx: 0,
                    lazy: 0,
                })
                .collect(),
        };
        st.build(1, 0, n);
        st
    }

    fn build(&mut self, u: usize, l: i32, r: i32) {
        self.tr[u] = Node {
            l,
            r,
            mn: 0,
            mx: 0,
            lazy: 0,
        };
        if l == r {
            return;
        }
        let mid = (l + r) >> 1;
        self.build(u << 1, l, mid);
        self.build(u << 1 | 1, mid + 1, r);
    }

    fn apply(&mut self, u: usize, v: i32) {
        self.tr[u].mn += v;
        self.tr[u].mx += v;
        self.tr[u].lazy += v;
    }

    fn pushup(&mut self, u: usize) {
        self.tr[u].mn = self.tr[u << 1].mn.min(self.tr[u << 1 | 1].mn);
        self.tr[u].mx = self.tr[u << 1].mx.max(self.tr[u << 1 | 1].mx);
    }

    fn pushdown(&mut self, u: usize) {
        if self.tr[u].lazy != 0 {
            let v = self.tr[u].lazy;
            self.apply(u << 1, v);
            self.apply(u << 1 | 1, v);
            self.tr[u].lazy = 0;
        }
    }

    fn modify(&mut self, u: usize, l: i32, r: i32, v: i32) {
        if self.tr[u].l >= l && self.tr[u].r <= r {
            self.apply(u, v);
            return;
        }
        self.pushdown(u);
        let mid = (self.tr[u].l + self.tr[u].r) >> 1;
        if l <= mid {
            self.modify(u << 1, l, r, v);
        }
        if r > mid {
            self.modify(u << 1 | 1, l, r, v);
        }
        self.pushup(u);
    }

    fn query(&mut self, u: usize, target: i32) -> i32 {
        if self.tr[u].l == self.tr[u].r {
            return self.tr[u].l;
        }
        self.pushdown(u);
        let left = u << 1;
        let right = u << 1 | 1;
        if self.tr[left].mn <= target && target <= self.tr[left].mx {
            self.query(left, target)
        } else {
            self.query(right, target)
        }
    }
}

impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        let mut st = SegmentTree::new(n);
        let mut last = HashMap::new();
        let mut now = 0;
        let mut ans = 0;
        for i in 1..=n {
            let x = nums[(i - 1) as usize];
            let det = if (x & 1) != 0 { 1 } else { -1 };
            if let Some(&prev) = last.get(&x) {
                st.modify(1, prev, n, -det);
                now -= det;
            }
            last.insert(x, i);
            st.modify(1, i, n, det);
            now += det;
            let pos = st.query(1, now);
            ans = ans.max(i - pos);
        }
        ans
    }
}
