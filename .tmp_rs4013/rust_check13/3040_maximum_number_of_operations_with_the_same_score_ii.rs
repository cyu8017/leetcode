#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3040 - Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        fn g(nums: &[i32], i0: usize, j0: i32, s: i32) -> i32 {
            let n = nums.len();
            if j0 < 0 {
                return 0;
            }
            let j0 = j0 as usize;
            let mut f = vec![vec![-1i32; n]; n];
            fn dfs(i: usize, j: usize, s: i32, nums: &[i32], f: &mut [Vec<i32>]) -> i32 {
                if j < i || j - i < 1 {
                    return 0;
                }
                if f[i][j] != -1 {
                    return f[i][j];
                }
                let mut ans = 0;
                if i + 1 <= j && nums[i] + nums[i + 1] == s {
                    ans = ans.max(1 + dfs(i + 2, j, s, nums, f));
                }
                if nums[i] + nums[j] == s {
                    if j >= 1 {
                        ans = ans.max(1 + dfs(i + 1, j - 1, s, nums, f));
                    }
                }
                if j >= 1 && nums[j - 1] + nums[j] == s {
                    if j >= 2 {
                        ans = ans.max(1 + dfs(i, j - 2, s, nums, f));
                    } else {
                        ans = ans.max(1);
                    }
                }
                f[i][j] = ans;
                ans
            }
            dfs(i0, j0, s, nums, &mut f)
        }
        let a = g(&nums, 2, n as i32 - 1, nums[0] + nums[1]);
        let b = g(&nums, 0, n as i32 - 3, nums[n - 1] + nums[n - 2]);
        let c = g(&nums, 1, n as i32 - 2, nums[0] + nums[n - 1]);
        1 + a.max(b).max(c)
    }
}
