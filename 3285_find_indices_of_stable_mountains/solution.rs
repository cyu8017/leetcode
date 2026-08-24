// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

impl Solution {
    pub fn stable_mountains(height: Vec<i32>, threshold: i32) -> Vec<i32> {
        let mut ans = Vec::new();
        for i in 1..height.len() {
            if height[i - 1] > threshold {
                ans.push(i as i32);
            }
        }
        ans
    }
}
