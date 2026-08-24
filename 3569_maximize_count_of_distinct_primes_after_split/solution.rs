// LeetCode 3569 - Maximize Count of Distinct Primes After Split
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_count(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut mx = *nums.iter().max().unwrap_or(&0);
        for q in &queries {
            mx = mx.max(q[1]);
        }
        let mx = mx as usize;
        let mut is_p = vec![false; mx + 1];
        for i in 2..=mx {
            is_p[i] = true;
        }
        let mut i = 2;
        while i * i <= mx {
            if is_p[i] {
                let mut j = i * i;
                while j <= mx {
                    is_p[j] = false;
                    j += i;
                }
            }
            i += 1;
        }
        let mut ans = vec![0; queries.len()];
        for (qi, q) in queries.iter().enumerate() {
            nums[q[0] as usize] = q[1];
            let mut best = 0;
            let mut left: HashMap<i32, i32> = HashMap::new();
            let mut right: HashMap<i32, i32> = HashMap::new();
            for &v in &nums {
                if v as usize <= mx && is_p[v as usize] {
                    *right.entry(v).or_insert(0) += 1;
                }
            }
            for i in 0..nums.len() - 1 {
                let v = nums[i];
                if v as usize <= mx && is_p[v as usize] {
                    *left.entry(v).or_insert(0) += 1;
                    if let Some(c) = right.get_mut(&v) {
                        *c -= 1;
                        if *c == 0 {
                            right.remove(&v);
                        }
                    }
                }
                best = best.max(left.len() as i32 + right.len() as i32);
            }
            ans[qi] = best;
        }
        ans
    }
}
