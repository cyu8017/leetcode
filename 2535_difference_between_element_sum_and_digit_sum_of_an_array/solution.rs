// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

impl Solution {
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut elem = 0;
        let mut digit = 0;
        for mut x in nums {
            elem += x;
            while x > 0 {
                digit += x % 10;
                x /= 10;
            }
        }
        (elem - digit).abs()
    }
}
