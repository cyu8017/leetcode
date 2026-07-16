// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut right = height.len() - 1;
        let mut best = 0;

        while left < right {
            let width = (right - left) as i32;
            let h = height[left].min(height[right]);
            best = best.max(h * width);
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        best
    }
}
