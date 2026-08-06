// LeetCode 1909 - Remove One Element to Make the Array Strictly Increasing
// https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

impl Solution {
    pub fn can_be_increasing(nums: Vec<i32>) -> bool {
        fn check(nums: &[i32], skip: usize) -> bool {
            let mut prev: Option<i32> = None;
            for (i, &x) in nums.iter().enumerate() {
                if i == skip {
                    continue;
                }
                if let Some(p) = prev {
                    if x <= p {
                        return false;
                    }
                }
                prev = Some(x);
            }
            true
        }

        for i in 1..nums.len() {
            if nums[i] <= nums[i - 1] {
                return check(&nums, i - 1) || check(&nums, i);
            }
        }
        true
    }
}
