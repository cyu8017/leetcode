// LeetCode 2104 - Sum of Subarray Ranges
// https://leetcode.com/problems/sum-of-subarray-ranges/

impl Solution {
    pub fn sub_array_ranges(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0i64;
        for i in 0..n {
            let mut mn = nums[i];
            let mut mx = nums[i];
            for j in i..n {
                mn = mn.min(nums[j]);
                mx = mx.max(nums[j]);
                ans += (mx - mn) as i64;
            }
        }
        ans
    }
}
