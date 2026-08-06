// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

impl Solution {
    pub fn max_value_after_reverse(nums: Vec<i32>) -> i32 {
        let base: i32 = nums.windows(2).map(|w| (w[0] - w[1]).abs()).sum();
        let mut gain = 0;
        let mut low = i32::MAX;
        let mut high = i32::MIN;
        for w in nums.windows(2) {
            let (a, b) = (w[0], w[1]);
            gain = gain
                .max((nums[0] - b).abs() - (a - b).abs())
                .max((nums[nums.len() - 1] - a).abs() - (a - b).abs());
            low = low.min(a.max(b));
            high = high.max(a.min(b));
        }
        base + gain.max(2 * (high - low))
    }
}
