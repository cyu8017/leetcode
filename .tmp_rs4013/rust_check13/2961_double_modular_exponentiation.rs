#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2961 - Double Modular Exponentiation
// https://leetcode.com/problems/double-modular-exponentiation/

impl Solution {
    pub fn get_good_indices(variables: Vec<Vec<i32>>, target: i32) -> Vec<i32> {
        fn mod_pow(mut a: i64, mut b: i64, m: i64) -> i64 {
            let mut res = 1 % m;
            a %= m;
            while b > 0 {
                if b & 1 == 1 {
                    res = res * a % m;
                }
                a = a * a % m;
                b >>= 1;
            }
            res
        }
        let mut ans = Vec::new();
        for (i, v) in variables.iter().enumerate() {
            let a = v[0] as i64;
            let b = v[1] as i64;
            let c = v[2] as i64;
            let m = v[3] as i64;
            if mod_pow(mod_pow(a, b, 10), c, m) == target as i64 {
                ans.push(i as i32);
            }
        }
        ans
    }
}
