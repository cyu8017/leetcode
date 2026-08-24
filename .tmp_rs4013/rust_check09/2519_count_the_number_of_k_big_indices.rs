struct Solution;

// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

use std::collections::HashMap;

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Self { bit: vec![0; n + 2] }
    }
    fn add(&mut self, mut i: usize, v: i32) {
        while i < self.bit.len() {
            self.bit[i] += v;
            i += i & i.wrapping_neg();
        }
    }
    fn sum(&self, mut i: usize) -> i32 {
        let mut s = 0;
        while i > 0 {
            s += self.bit[i];
            i -= i & i.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn k_big_indices(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut uniq = nums.clone();
        uniq.sort_unstable();
        uniq.dedup();
        let mut rank = HashMap::new();
        for (i, &v) in uniq.iter().enumerate() {
            rank.insert(v, i + 1);
        }
        let m = uniq.len();
        let mut left = vec![0; n];
        let mut right = vec![0; n];
        let mut ft = Fenwick::new(m);
        for i in 0..n {
            let r = rank[&nums[i]];
            left[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        let mut ft = Fenwick::new(m);
        for i in (0..n).rev() {
            let r = rank[&nums[i]];
            right[i] = ft.sum(r - 1);
            ft.add(r, 1);
        }
        let mut ans = 0;
        for i in 0..n {
            if left[i] >= k && right[i] >= k {
                ans += 1;
            }
        }
        ans
    }
}

fn main() {}
