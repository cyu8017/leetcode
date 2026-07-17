// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

impl Solution {
    pub fn find_buildings(heights: Vec<i32>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();
        let mut tallest = 0;
        for i in (0..heights.len()).rev() {
            if heights[i] > tallest {
                ans.push(i as i32);
                tallest = heights[i];
            }
        }
        ans.reverse();
        ans
    }
}
