#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3018 - Maximum Number of Removal Queries That Can Be Processed I
// https://leetcode.com/problems/maximum-number-of-removal-queries-that-can-be-processed-i/

impl Solution {
    pub fn maximum_processable_queries(nums: Vec<i32>, queries: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut f = vec![vec![0; n]; n];
        let m = queries.len();
        for i in 0..n {
            for j in (i..n).rev() {
                if i > 0 {
                    let qi = f[i - 1][j] as usize;
                    if qi >= m {
                        return m as i32;
                    }
                    let t = if nums[i - 1] >= queries[qi] { 1 } else { 0 };
                    f[i][j] = f[i][j].max(f[i - 1][j] + t);
                }
                if j + 1 < n {
                    let qi = f[i][j + 1] as usize;
                    if qi >= m {
                        return m as i32;
                    }
                    let t = if nums[j + 1] >= queries[qi] { 1 } else { 0 };
                    f[i][j] = f[i][j].max(f[i][j + 1] + t);
                }
                if f[i][j] == m as i32 {
                    return m as i32;
                }
            }
        }
        let mut ans = 0;
        for i in 0..n {
            let qi = f[i][i] as usize;
            if qi >= m {
                return m as i32;
            }
            let t = if nums[i] >= queries[qi] { 1 } else { 0 };
            ans = ans.max(f[i][i] + t);
        }
        ans
    }
}
