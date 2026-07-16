// LeetCode 0485 - Max Consecutive Ones
// https://leetcode.com/problems/max-consecutive-ones/

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut best = 0;
        let mut current = 0;
        for num in nums {
            if num == 1 {
                current += 1;
                best = best.max(current);
            } else {
                current = 0;
            }
        }
        best
    }
}
