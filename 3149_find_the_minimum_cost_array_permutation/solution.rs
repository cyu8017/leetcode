// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

impl Solution {
    pub fn find_permutation(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut memo = vec![vec![-1i32; n]; 1 << n];
        fn dfs(nums: &[i32], n: usize, mask: usize, pre: usize, memo: &mut [Vec<i32>]) -> i32 {
            if mask == (1 << n) - 1 {
                return (pre as i32 - nums[0]).abs();
            }
            if memo[mask][pre] != -1 {
                return memo[mask][pre];
            }
            let mut res = i32::MAX;
            for cur in 1..n {
                if (mask >> cur) & 1 == 0 {
                    res = res.min((pre as i32 - nums[cur]).abs() + dfs(nums, n, mask | (1 << cur), cur, memo));
                }
            }
            memo[mask][pre] = res;
            res
        }
        let mut ans = Vec::new();
        fn g(
            nums: &[i32],
            n: usize,
            mask: usize,
            pre: usize,
            memo: &mut [Vec<i32>],
            ans: &mut Vec<i32>,
        ) {
            ans.push(pre as i32);
            if mask == (1 << n) - 1 {
                return;
            }
            let res = dfs(nums, n, mask, pre, memo);
            for cur in 1..n {
                if (mask >> cur) & 1 == 0 {
                    if (pre as i32 - nums[cur]).abs() + dfs(nums, n, mask | (1 << cur), cur, memo) == res {
                        g(nums, n, mask | (1 << cur), cur, memo, ans);
                        break;
                    }
                }
            }
        }
        g(&nums, n, 1, 0, &mut memo, &mut ans);
        ans
    }
}
