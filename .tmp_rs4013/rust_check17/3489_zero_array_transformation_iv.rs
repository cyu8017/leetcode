struct Solution;
// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

impl Solution {
    fn can_subset_sum(vals: &[i32], target: i32) -> bool {
        if target == 0 {
            return true;
        }
        let mut dp = vec![false; (target + 1) as usize];
        dp[0] = true;
        for &v in vals {
            for s in (v..=target).rev() {
                if dp[(s - v) as usize] {
                    dp[s as usize] = true;
                }
            }
        }
        dp[target as usize]
    }

    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let ok = |k: i32| -> bool {
            for i in 0..n {
                if nums[i] == 0 {
                    continue;
                }
                let mut vals = Vec::new();
                for q in 0..k as usize {
                    let l = queries[q][0];
                    let r = queries[q][1];
                    let v = queries[q][2];
                    if l <= i as i32 && i as i32 <= r {
                        vals.push(v);
                    }
                }
                if !Self::can_subset_sum(&vals, nums[i]) {
                    return false;
                }
            }
            true
        };
        if ok(0) {
            return 0;
        }
        let mut lo = 1;
        let mut hi = queries.len() as i32 + 1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if mid <= queries.len() as i32 && ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if lo > queries.len() as i32 {
            -1
        } else {
            lo
        }
    }
}

fn main() {}
