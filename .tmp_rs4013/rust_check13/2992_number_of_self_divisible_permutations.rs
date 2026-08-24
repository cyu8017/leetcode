#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

impl Solution {
    pub fn self_divisible_permutation_count(n: i32) -> i32 {
        let mut ans = 0;
        let mut used = vec![false; (n + 1) as usize];
        fn dfs(pos: i32, n: i32, used: &mut [bool], ans: &mut i32) {
            if pos > n {
                *ans += 1;
                return;
            }
            for v in 1..=n {
                if used[v as usize] {
                    continue;
                }
                if gcd(v, pos) != 1 {
                    continue;
                }
                used[v as usize] = true;
                dfs(pos + 1, n, used, ans);
                used[v as usize] = false;
            }
        }
        dfs(1, n, &mut used, &mut ans);
        ans
    }
}
