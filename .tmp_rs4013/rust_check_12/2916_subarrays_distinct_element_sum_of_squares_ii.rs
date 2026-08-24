struct Solution;
// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

use std::collections::HashMap;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut last: HashMap<i32, usize> = HashMap::new();
        #[derive(Clone, Copy, Default)]
        struct Node {
            sum: i32,
            sum_sq: i32,
            lazy: i32,
        }
        let mut tree = vec![Node::default(); 4 * (n + 2)];
        fn apply(tree: &mut [Node], idx: usize, l: usize, r: usize, val: i32) {
            let length = (r - l + 1) as i64;
            let val = val as i64;
            tree[idx].sum_sq = ((tree[idx].sum_sq as i64
                + 2 * val % MOD * tree[idx].sum as i64 % MOD
                + val % MOD * val % MOD * length % MOD)
                % MOD) as i32;
            tree[idx].sum = ((tree[idx].sum as i64 + val % MOD * length % MOD) % MOD) as i32;
            tree[idx].lazy = ((tree[idx].lazy as i64 + val) % MOD) as i32;
        }
        fn update(tree: &mut [Node], idx: usize, l: usize, r: usize, ql: usize, qr: usize, val: i32) {
            if ql > r || qr < l {
                return;
            }
            if ql <= l && r <= qr {
                apply(tree, idx, l, r, val);
                return;
            }
            if tree[idx].lazy != 0 && l != r {
                let mid = (l + r) / 2;
                apply(tree, idx * 2, l, mid, tree[idx].lazy);
                apply(tree, idx * 2 + 1, mid + 1, r, tree[idx].lazy);
                tree[idx].lazy = 0;
            }
            let mid = (l + r) / 2;
            update(tree, idx * 2, l, mid, ql, qr, val);
            update(tree, idx * 2 + 1, mid + 1, r, ql, qr, val);
            tree[idx].sum = (tree[idx * 2].sum + tree[idx * 2 + 1].sum) % MOD as i32;
            tree[idx].sum_sq = (tree[idx * 2].sum_sq + tree[idx * 2 + 1].sum_sq) % MOD as i32;
        }
        let mut ans = 0i32;
        for i in 1..=n {
            let v = nums[i - 1];
            let prev = *last.get(&v).unwrap_or(&0);
            update(&mut tree, 1, 1, n, prev + 1, i, 1);
            ans = (ans + tree[1].sum_sq) % MOD as i32;
            last.insert(v, i);
        }
        ans
    }
}

fn main() {}
