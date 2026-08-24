struct Solution;

// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

impl Solution {
    pub fn make_sub_k_sum_equal(arr: Vec<i32>, k: i32) -> i64 {
        fn gcd(mut a: usize, mut b: usize) -> usize {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a
        }
        let n = arr.len();
        let g = gcd(n, k as usize);
        let mut ans = 0i64;
        for r in 0..g {
            let mut group = Vec::new();
            let mut i = r;
            while i < n {
                group.push(arr[i]);
                i += g;
            }
            group.sort_unstable();
            let med = group[group.len() / 2];
            for x in group {
                ans += (x - med).abs() as i64;
            }
        }
        ans
    }
}

fn main() {}
