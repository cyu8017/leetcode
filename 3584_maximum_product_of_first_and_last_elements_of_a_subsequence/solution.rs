// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

impl Solution {
    pub fn maximum_product(nums: Vec<i32>, m: i32) -> i64 {
        let mut ans = i64::MIN;
        let mut mx = i32::MIN;
        let mut mi = i32::MAX;
        for i in (m as usize - 1)..nums.len() {
            let x = nums[i];
            let y = nums[i - m as usize + 1];
            mi = mi.min(y);
            mx = mx.max(y);
            ans = ans.max((x as i64 * mi as i64).max(x as i64 * mx as i64));
        }
        ans
    }
}
