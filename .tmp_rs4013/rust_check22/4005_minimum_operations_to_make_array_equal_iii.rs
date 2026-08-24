struct Solution;
// LeetCode 4005 - Minimum Operations to Make Array Equal III
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-iii/

use std::collections::BTreeSet;

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn cost(x: i32, t: i32) -> i32 {
    if x == t {
        0
    } else if x % t == 0 || t % x == 0 {
        1
    } else {
        2
    }
}

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n <= 1 {
            return 0;
        }
        let mut g = nums[0];
        let mut mn = nums[0];
        for &x in nums.iter().skip(1) {
            g = gcd(g, x);
            mn = mn.min(x);
        }
        let mut cands = BTreeSet::new();
        for &x in &nums {
            cands.insert(x);
        }
        let mut d = 1i32;
        while d as i64 * d as i64 <= mn as i64 {
            if mn % d == 0 {
                cands.insert(d);
                cands.insert(mn / d);
            }
            d += 1;
        }
        cands.insert(g);
        let mut ans = i32::MAX;
        for &t in &cands {
            let mut sum = 0;
            for &x in &nums {
                sum += cost(x, t);
                if sum >= ans {
                    break;
                }
            }
            ans = ans.min(sum);
        }
        ans
    }
}

fn main() {}
