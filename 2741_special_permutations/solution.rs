// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

impl Solution {
    pub fn special_perm(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = nums.len();
        let mut memo = vec![vec![-1i32; n]; 1 << n];
        fn dfs(
            mask: usize,
            last: usize,
            nums: &[i32],
            memo: &mut [Vec<i32>],
            n: usize,
        ) -> i32 {
            if mask == (1 << n) - 1 {
                return 1;
            }
            if memo[mask][last] != -1 {
                return memo[mask][last];
            }
            let mut res = 0;
            for i in 0..n {
                if mask & (1 << i) != 0 {
                    continue;
                }
                if nums[i] % nums[last] == 0 || nums[last] % nums[i] == 0 {
                    res = (res + dfs(mask | (1 << i), i, nums, memo, n)) % MOD;
                }
            }
            memo[mask][last] = res;
            res
        }
        let mut ans = 0;
        for i in 0..n {
            ans = (ans + dfs(1 << i, i, &nums, &mut memo, n)) % MOD;
        }
        ans
    }
}
