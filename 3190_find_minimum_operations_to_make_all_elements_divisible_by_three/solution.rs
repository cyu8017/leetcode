// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.iter().filter(|&&x| x % 3 != 0).count() as i32
    }
}
