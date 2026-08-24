// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

impl Solution {
    pub fn smallest_index(nums: Vec<i32>) -> i32 {
        for (i, &num) in nums.iter().enumerate() {
            let mut x = num;
            let mut s = 0;
            while x > 0 {
                s += x % 10;
                x /= 10;
            }
            if s == i as i32 {
                return i as i32;
            }
        }
        -1
    }
}
