// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let mut xor_all = 0;
        for num in &nums {
            xor_all ^= num;
        }
        let diff = xor_all & -xor_all;
        let mut first = 0;
        let mut second = 0;
        for num in nums {
            if num & diff != 0 {
                first ^= num;
            } else {
                second ^= num;
            }
        }
        vec![first, second]
    }
}
