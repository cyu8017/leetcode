// LeetCode 0410 - Split Array Largest Sum
// https://leetcode.com/problems/split-array-largest-sum/

impl Solution {
    pub fn split_array(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = *nums.iter().max().unwrap();
        let mut right: i32 = nums.iter().sum();

        while left < right {
            let mid = left + (right - left) / 2;
            if Self::can_split(&nums, k, mid) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        left
    }

    fn can_split(nums: &[i32], k: i32, limit: i32) -> bool {
        let mut parts = 1;
        let mut current = 0;

        for &value in nums {
            if current + value > limit {
                parts += 1;
                current = 0;
            }
            current += value;
        }

        parts <= k
    }
}
