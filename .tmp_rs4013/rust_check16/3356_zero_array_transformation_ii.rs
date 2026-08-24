struct Solution;
// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

impl Solution {
    pub fn min_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        let n = nums.len();
        let ok = |k: usize| -> bool {
            let mut diff = vec![0i64; n + 1];
            for i in 0..k {
                let q = &queries[i];
                diff[q[0] as usize] += q[2] as i64;
                diff[q[1] as usize + 1] -= q[2] as i64;
            }
            let mut cur = 0i64;
            for i in 0..n {
                cur += diff[i];
                if cur < nums[i] as i64 {
                    return false;
                }
            }
            true
        };
        if ok(0) {
            return 0;
        }
        let mut lo = 1;
        let mut hi = queries.len() + 1;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if mid <= queries.len() && ok(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if lo > queries.len() {
            -1
        } else {
            lo as i32
        }
    }
}

fn main() {}
