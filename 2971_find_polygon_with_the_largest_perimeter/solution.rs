// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

impl Solution {
    pub fn largest_perimeter(mut nums: Vec<i32>) -> i64 {
        nums.sort_unstable();
        let mut sum: i64 = nums.iter().map(|&v| v as i64).sum();
        for i in (2..nums.len()).rev() {
            sum -= nums[i] as i64;
            if sum > nums[i] as i64 {
                return sum + nums[i] as i64;
            }
        }
        -1
    }
}
