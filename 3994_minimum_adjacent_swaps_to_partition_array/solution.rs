// LeetCode 3994 - Minimum Adjacent Swaps to Partition Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-partition-array/

impl Solution {
    pub fn min_adjacent_swaps(nums: Vec<i32>, a: i32, b: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut result = 0;
        let mut cnt1 = 0;
        let mut cnt2 = 0;
        for x in nums {
            if x < a {
                result = (result + cnt1 + cnt2) % MOD;
            } else if x <= b {
                cnt1 += 1;
                result = (result + cnt2) % MOD;
            } else {
                cnt2 += 1;
            }
        }
        result
    }
}
