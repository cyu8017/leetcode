struct Solution;
// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut f = vec![vec![0; k + 1]; n];
        let mut mp: Vec<HashMap<i32, i32>> = vec![HashMap::new(); k + 1];
        let mut g = vec![[0; 3]; k + 1];
        let mut ans = 0;
        for i in 0..n {
            for h in 0..=k {
                f[i][h] = *mp[h].get(&nums[i]).unwrap_or(&0);
                if h > 0 {
                    if g[h - 1][0] != nums[i] {
                        f[i][h] = f[i][h].max(g[h - 1][1]);
                    } else {
                        f[i][h] = f[i][h].max(g[h - 1][2]);
                    }
                }
                f[i][h] += 1;
                let e = mp[h].entry(nums[i]).or_insert(0);
                *e = (*e).max(f[i][h]);
                if g[h][0] != nums[i] {
                    if f[i][h] >= g[h][1] {
                        g[h][2] = g[h][1];
                        g[h][1] = f[i][h];
                        g[h][0] = nums[i];
                    } else if f[i][h] > g[h][2] {
                        g[h][2] = f[i][h];
                    }
                } else if f[i][h] > g[h][1] {
                    g[h][1] = f[i][h];
                }
                ans = ans.max(f[i][h]);
            }
        }
        ans
    }
}

fn main() {}
