// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

impl Solution {
    pub fn pour_water(mut heights: Vec<i32>, volume: i32, k: i32) -> Vec<i32> {
        let k = k as usize;
        for _ in 0..volume {
            let mut index = k;
            for i in (0..k).rev() {
                if heights[i] > heights[index] {
                    break;
                }
                if heights[i] < heights[index] {
                    index = i;
                }
            }
            if index != k {
                heights[index] += 1;
                continue;
            }
            index = k;
            for i in k + 1..heights.len() {
                if heights[i] > heights[index] {
                    break;
                }
                if heights[i] < heights[index] {
                    index = i;
                }
            }
            heights[index] += 1;
        }
        heights
    }
}
