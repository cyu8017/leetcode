#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

use std::collections::HashMap;

impl Solution {
    pub fn most_frequent_prime(mat: Vec<Vec<i32>>) -> i32 {
        fn is_prime(n: i32) -> bool {
            if n < 2 {
                return false;
            }
            let mut i = 2;
            while i <= n / i {
                if n % i == 0 {
                    return false;
                }
                i += 1;
            }
            true
        }
        let m = mat.len() as i32;
        let n = mat[0].len() as i32;
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for i in 0..m {
            for j in 0..n {
                for a in -1..=1 {
                    for b in -1..=1 {
                        if a == 0 && b == 0 {
                            continue;
                        }
                        let mut x = i + a;
                        let mut y = j + b;
                        let mut v = mat[i as usize][j as usize];
                        while x >= 0 && x < m && y >= 0 && y < n {
                            v = v * 10 + mat[x as usize][y as usize];
                            if is_prime(v) {
                                *cnt.entry(v).or_insert(0) += 1;
                            }
                            x += a;
                            y += b;
                        }
                    }
                }
            }
        }
        let mut ans = -1;
        let mut mx = 0;
        for (&v, &x) in &cnt {
            if mx < x || (mx == x && ans < v) {
                mx = x;
                ans = v;
            }
        }
        ans
    }
}
