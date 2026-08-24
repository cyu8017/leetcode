struct Solution;
fn main() {}

// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

impl Solution {
    pub fn number_of_good_subarray_splits(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let ones: Vec<usize> = nums
            .iter()
            .enumerate()
            .filter(|(_, &v)| v == 1)
            .map(|(i, _)| i)
            .collect();
        if ones.is_empty() {
            return 0;
        }
        let mut ans = 1i64;
        for i in 1..ones.len() {
            ans = ans * (ones[i] - ones[i - 1]) as i64 % MOD;
        }
        ans as i32
    }
}
