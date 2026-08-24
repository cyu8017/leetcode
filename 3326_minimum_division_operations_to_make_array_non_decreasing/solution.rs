// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

impl Solution {
    fn smallest_proper_divisor(x: i32) -> i32 {
        let mut d = 2;
        while d * d <= x {
            if x % d == 0 {
                return d;
            }
            d += 1;
        }
        x
    }

    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        let mut ops = 0;
        for i in (0..nums.len() - 1).rev() {
            if nums[i] <= nums[i + 1] {
                continue;
            }
            while nums[i] > nums[i + 1] {
                let d = Self::smallest_proper_divisor(nums[i]);
                if d == nums[i] {
                    return -1;
                }
                nums[i] /= d;
                ops += 1;
                if nums[i] > nums[i + 1] && Self::smallest_proper_divisor(nums[i]) == nums[i] {
                    return -1;
                }
            }
        }
        ops
    }
}
