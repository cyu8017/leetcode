// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

impl Solution {
    pub fn num_of_ways(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut choose = vec![vec![0i64; n + 1]; n + 1];
        for i in 0..=n {
            choose[i][0] = 1;
            choose[i][i] = 1;
            for j in 1..i {
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
            }
        }
        fn ways(values: &[i32], choose: &[Vec<i64>]) -> i64 {
            if values.len() < 3 {
                return 1;
            }
            let left: Vec<i32> = values[1..].iter().copied().filter(|&x| x < values[0]).collect();
            let right: Vec<i32> = values[1..].iter().copied().filter(|&x| x > values[0]).collect();
            choose[values.len() - 1][left.len()] * ways(&left, choose) % MOD * ways(&right, choose)
                % MOD
        }
        ((ways(&nums, &choose) - 1 + MOD) % MOD) as i32
    }
}
