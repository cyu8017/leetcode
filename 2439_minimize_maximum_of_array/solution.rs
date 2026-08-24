// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

impl Solution {
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        let mut sum = 0i64;
        let mut ans = 0;
        for (i, &x) in nums.iter().enumerate() {
            sum += x as i64;
            let avg = ((sum + i as i64) / (i as i64 + 1)) as i32;
            if avg > ans {
                ans = avg;
            }
        }
        ans
    }
}
