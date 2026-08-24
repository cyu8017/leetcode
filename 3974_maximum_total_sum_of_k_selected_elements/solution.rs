// LeetCode 3974 - Maximum Total Sum Of K Selected Elements
// https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

impl Solution {
    pub fn max_sum(mut nums: Vec<i32>, k: i32, mut mul: i32) -> i64 {
        nums.sort_unstable();
        let n = nums.len();
        let mut ans = 0i64;
        for i in ((n - k as usize)..n).rev() {
            let m = 1.max(mul);
            ans += nums[i] as i64 * m as i64;
            mul -= 1;
        }
        ans
    }
}
