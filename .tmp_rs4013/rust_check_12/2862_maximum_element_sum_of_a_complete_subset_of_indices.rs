struct Solution;
// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i64 {
        fn square_free(mut x: i32) -> i32 {
            let mut res = 1;
            let mut p = 2;
            while p * p <= x {
                let mut cnt = 0;
                while x % p == 0 {
                    x /= p;
                    cnt += 1;
                }
                if cnt % 2 == 1 {
                    res *= p;
                }
                p += 1;
            }
            if x > 1 {
                res *= x;
            }
            res
        }
        let n = nums.len();
        let mut groups: HashMap<i32, i64> = HashMap::new();
        let mut ans = 0i64;
        for i in 1..=n {
            let sf = square_free(i as i32);
            let e = groups.entry(sf).or_insert(0);
            *e += nums[i - 1] as i64;
            if *e > ans {
                ans = *e;
            }
        }
        ans
    }
}

fn main() {}
