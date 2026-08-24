// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

use std::collections::HashMap;

impl Solution {
    pub fn find_valid_split(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut first = HashMap::new();
        let mut last = HashMap::new();
        let factorize = |x: i32, idx: usize, first: &mut HashMap<i32, usize>, last: &mut HashMap<i32, usize>| {
            let mut x = x;
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    first.entry(p).or_insert(idx);
                    last.insert(p, idx);
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                first.entry(x).or_insert(idx);
                last.insert(x, idx);
            }
        };
        for i in 0..n {
            factorize(nums[i], i, &mut first, &mut last);
        }
        let mut far = 0usize;
        for i in 0..n - 1 {
            let mut x = nums[i];
            let mut p = 2;
            while p * p <= x {
                if x % p == 0 {
                    if let Some(&lf) = last.get(&p) {
                        if lf > far {
                            far = lf;
                        }
                    }
                    while x % p == 0 {
                        x /= p;
                    }
                }
                p += 1;
            }
            if x > 1 {
                if let Some(&lf) = last.get(&x) {
                    if lf > far {
                        far = lf;
                    }
                }
            }
            if far == i {
                return i as i32;
            }
        }
        -1
    }
}
