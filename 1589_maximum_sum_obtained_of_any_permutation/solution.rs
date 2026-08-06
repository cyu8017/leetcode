// LeetCode 1589 - Maximum Sum Obtained of Any Permutation
// https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

impl Solution {
    pub fn max_sum_range_query(mut nums: Vec<i32>, requests: Vec<Vec<i32>>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len();
        let mut diff = vec![0i32; n + 1];
        for req in requests {
            diff[req[0] as usize] += 1;
            diff[req[1] as usize + 1] -= 1;
        }
        for i in 1..n {
            diff[i] += diff[i - 1];
        }
        nums.sort_unstable();
        let mut freq: Vec<i32> = diff[..n].to_vec();
        freq.sort_unstable();
        (nums
            .iter()
            .zip(freq.iter())
            .map(|(&a, &b)| a as i64 * b as i64)
            .sum::<i64>()
            % MOD) as i32
    }
}
