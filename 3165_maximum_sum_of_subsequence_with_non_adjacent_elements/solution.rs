// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

#[derive(Clone, Copy, Default)]
struct Node {
    l: i32,
    r: i32,
    s00: i32,
    s01: i32,
    s10: i32,
    s11: i32,
}

impl Solution {
    fn build(tr: &mut [Node], u: usize, l: i32, r: i32) {
        tr[u].l = l;
        tr[u].r = r;
        if l == r {
            return;
        }
        let mid = (l + r) >> 1;
        Self::build(tr, u << 1, l, mid);
        Self::build(tr, u << 1 | 1, mid + 1, r);
    }

    fn pushup(tr: &mut [Node], u: usize) {
        let left = tr[u << 1];
        let right = tr[u << 1 | 1];
        tr[u].s00 = (left.s00 + right.s10).max(left.s01 + right.s00);
        tr[u].s01 = (left.s00 + right.s11).max(left.s01 + right.s01);
        tr[u].s10 = (left.s10 + right.s10).max(left.s11 + right.s00);
        tr[u].s11 = (left.s10 + right.s11).max(left.s11 + right.s01);
    }

    fn modify(tr: &mut [Node], u: usize, x: i32, v: i32) {
        if tr[u].l == tr[u].r {
            tr[u].s11 = 0.max(v);
            return;
        }
        let mid = (tr[u].l + tr[u].r) >> 1;
        if x <= mid {
            Self::modify(tr, u << 1, x, v);
        } else {
            Self::modify(tr, u << 1 | 1, x, v);
        }
        Self::pushup(tr, u);
    }

    fn query(tr: &[Node], u: usize, l: i32, r: i32) -> i32 {
        if tr[u].l >= l && tr[u].r <= r {
            return tr[u].s11;
        }
        let mid = (tr[u].l + tr[u].r) >> 1;
        let mut ans = 0;
        if r <= mid {
            ans = Self::query(tr, u << 1, l, r);
        }
        if l > mid {
            ans = ans.max(Self::query(tr, u << 1 | 1, l, r));
        }
        ans
    }

    pub fn maximum_sum_subsequence(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let mut tr = vec![Node::default(); n * 4];
        Self::build(&mut tr, 1, 1, n as i32);
        for i in 0..n {
            Self::modify(&mut tr, 1, i as i32 + 1, nums[i]);
        }
        const MOD: i32 = 1_000_000_007;
        let mut ans = 0;
        for q in queries {
            Self::modify(&mut tr, 1, q[0] + 1, q[1]);
            ans = (ans + Self::query(&tr, 1, 1, n as i32)) % MOD;
        }
        ans
    }
}
