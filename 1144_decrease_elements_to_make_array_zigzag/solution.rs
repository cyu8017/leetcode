// LeetCode 1144 - Decrease Elements To Make Array Zigzag
// https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

impl Solution {
    pub fn moves_to_make_zigzag(nums: Vec<i32>) -> i32 {
        let cost = |start: usize| -> i32 {
            let mut ans = 0;
            let mut i = start;
            while i < nums.len() {
                let left = if i > 0 { nums[i - 1] } else { i32::MAX };
                let right = if i + 1 < nums.len() {
                    nums[i + 1]
                } else {
                    i32::MAX
                };
                let limit = left.min(right);
                if nums[i] - limit + 1 > 0 {
                    ans += nums[i] - limit + 1;
                }
                i += 2;
            }
            ans
        };
        cost(0).min(cost(1))
    }
}
