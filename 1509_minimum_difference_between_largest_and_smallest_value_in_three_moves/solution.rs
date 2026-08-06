// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

impl Solution {
    pub fn min_difference(mut nums: Vec<i32>) -> i32 {
        if nums.len() <= 4 {
            return 0;
        }
        nums.sort_unstable();
        let n = nums.len();
        (0..4).map(|i| nums[n - 4 + i] - nums[i]).min().unwrap()
    }
}
