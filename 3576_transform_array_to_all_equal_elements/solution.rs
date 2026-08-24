// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

impl Solution {
    pub fn can_make_equal(nums: Vec<i32>, k: i32) -> bool {
        let check = |target: i32, kk: i32| -> bool {
            let mut cnt = 0;
            let mut sign = 1;
            for i in 0..nums.len() - 1 {
                let x = nums[i] * sign;
                if x == target {
                    sign = 1;
                } else {
                    sign = -1;
                    cnt += 1;
                }
            }
            cnt <= kk && nums[nums.len() - 1] * sign == target
        };
        check(nums[0], k) || check(-nums[0], k)
    }
}
