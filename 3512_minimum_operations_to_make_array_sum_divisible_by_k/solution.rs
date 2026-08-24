// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut ans = 0;
        for x in nums {
            ans = (ans + x) % k;
        }
        ans
    }
}
