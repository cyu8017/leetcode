// LeetCode 0041 - First Missing Positive
// https://leetcode.com/problems/first-missing-positive/

impl Solution {
    pub fn first_missing_positive(nums: &mut Vec<i32>) -> i32 {
        let n = nums.len();
        let mut i = 0;

        while i < n {
            let value = nums[i];
            let target = (value - 1) as usize;
            if (1..=n as i32).contains(&value) && nums[target] != value {
                nums.swap(i, target);
            } else {
                i += 1;
            }
        }

        for (index, &value) in nums.iter().enumerate() {
            if value != index as i32 + 1 {
                return index as i32 + 1;
            }
        }

        (n + 1) as i32
    }
}
