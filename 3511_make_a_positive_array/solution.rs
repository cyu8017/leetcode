// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

impl Solution {
    pub fn make_array_positive(nums: Vec<i32>) -> i32 {
        let mut ans = 0;
        let mut l = -1i32;
        let mut pre_mx = 0i64;
        let mut s = 0i64;
        for r in 0..nums.len() {
            s += nums[r] as i64;
            if r as i32 - l > 2 && s <= pre_mx {
                ans += 1;
                l = r as i32;
                pre_mx = 0;
                s = 0;
            } else if r as i32 - l >= 2 {
                pre_mx = pre_mx.max(s - nums[r] as i64 - nums[r - 1] as i64);
            }
        }
        ans
    }
}
